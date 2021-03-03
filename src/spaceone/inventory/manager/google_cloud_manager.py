__all__ = ['GoogleCloudManager']
import time
from pprint import pprint

import concurrent.futures
from spaceone.inventory.model.server import *
from spaceone.inventory.libs.manager import CollectorManager
_LOGGER = logging.getLogger(__name__)
MAX_WORKER = 20


class GoogleCloudManager(CollectorManager):
    provider = 'google_cloud'

    def collect_monitoring_data(self, params):
        print("**  Google Cloud monitoring collecting has started **\n")
        start_time = time.time()
        try:

            google_server_ids = params.get('server_ids').get(self.provider)
            google_servers = params.get('servers').get(self.provider)
            google_accounts = params.get('accounts').get(self.provider)

            with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
                future_executors = []
                for account in google_accounts:
                    print(f'@@@ Processing Google account : {account} @@@ \n')
                    _params = params.copy()
                    _params.update({
                        'server_ids': google_server_ids.get(account, []),
                        'servers': google_servers.get(account, []),
                        'account': account,
                    })
                    future_executors.append(executor.submit(self.collect_google_monitoring_dt_per_accounts, _params))

                for future in concurrent.futures.as_completed(future_executors):
                    for result in future.result():
                        yield result

        except Exception as e:
            print(f'[ERROR: {e}]')
            raise e

        print(f' Google Cloud Monitoring data collecting has Finished in  {time.time() - start_time} Seconds')

    def collect_google_monitoring_dt_per_accounts(self, params):
        _account = params.get('account')
        server_id_group = self.get_divided_into_max_count(MAX_WORKER, params.get('server_ids'))
        servers = self.get_divided_into_max_count(MAX_WORKER, params.get('servers'))
        _total_length = self._get_total_length(server_id_group)

        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
            future_executors = []
            for idx, server_ids in enumerate(server_id_group, start=0):
                print(f"@@@ Processing Google Cloud account:{_account}  {len(server_ids)}/{_total_length} @@@ \n")
                _params = params.copy()
                _params.update({
                    'server_ids': server_ids,
                    'servers': servers[idx],
                })
                future_executors.append(executor.submit(self.collect_google_monitoring_per_ids, _params))

            for future in concurrent.futures.as_completed(future_executors):
                for result in future.result():
                    yield result

    def collect_google_monitoring_per_ids(self, params):
        google_vm_resources = []
        # Check available resources
        server_ids = params.get('server_ids')
        servers = params.get('servers')

        try:
            resources_check = self.list_metrics(self.provider, 'inventory.Server', server_ids)
            available_resources = self._get_only_available_ids(resources_check.get('available_resources', {}),
                                                               server_ids)

            # Apply only server that is available for get_metric
            monitoring_data = self.get_servers_metric_data(params.get('metric_schema'),
                                                           self.provider,
                                                           available_resources,
                                                           self.start,
                                                           self.end) if available_resources else {}

            google_servers_vos = self.set_metric_data_to_server(params.get('metric_schema'),
                                                               servers,
                                                               monitoring_data)

            google_vm_resources.extend(google_servers_vos)

        except Exception as e:
            print(f'[ERROR: {e}]')
            raise e

        return google_vm_resources







