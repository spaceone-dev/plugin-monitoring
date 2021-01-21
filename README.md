# plugin-monitoring-metric-collector

Monitoring plugin collector categorized metric over clouds that includes aws, google cloud, azure

![SpaceONE](https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/spaceone/spaceone-logo.svg)

**Plugin to collect monitoring-metrics**

> SpaceONE's [plugin-google-cloud-services](https://github.com/spaceone-dev/plugin-monitoring-metric-collector) is a convenient tool to 
get monitoring metric data for following clouds:
>- AWS
>- Azure
>- Google Cloud 

Find us also at [Dockerhub](https://hub.docker.com/repository/docker/spaceone/monitoring-metric-collector)
> Latest stable version : 1.0

```
Note: Current version of plugin is limited to collect server type only for followings: 

- AWS (EC2)
- Azure (Compute VM)
- Google Cloud (Compute Instance)  

Other cloud service type will be available soon.  
```


Please contact us if you need any further information. (<support@spaceone.dev>)

---

## Authentication Overview
You must register SpaceONE's service account to run plugin 'Monitoring-metric-collector'.

Please, register ***SpaceONE service account credential*** in SpaceONE platform. 

Contact system admin if you need to issue a new service account credential.


## Monitoring Metrics
| Key  | Unit |AWS|Azure|Google Cloud|
| --------: |:----:|:----|:----| :----|
| cpu.utilization | (%) | CPUUtilization| Percentage CPU | compute.googleapis.com/instance/cpu/utilization |
| memory.usage | (%) |  |  |  |
| memory.total | (bytes) |  |  | compute.googleapis.com/instance/memory/balloon/ram_size |
| memory.used | (bytes) |  |  | compute.googleapis.com/instance/memory/balloon/ram_used |
| disk.write_iops | (counts)| DiskWriteOps, EBSWriteOps  | Data Disk Write Operations/Sec | compute.googleapis.com/instance/disk/write_ops_count |
| disk.write_throughput  | (bytes)| DiskWriteBytes, EBSWriteBytes  | Disk Write Bytes | compute.googleapis.com/instance/disk/write_bytes_count |
| disk.read_iops  | (counts)| DiskReadOps, EBSReadOps | Disk Read Operations/Sec | compute.googleapis.com/instance/disk/read_ops_count |
| disk.read_throughput  | (bytes)| DiskReadBytes, EBSReadBytes | Disk Read Bytes | compute.googleapis.com/instance/disk/read_bytes_count |
| network.received_throughput | (bytes)| NetworkPacketsIn | Network In | compute.googleapis.com/instance/network/received_bytes_count |
| network.received_pps | (counts)| NetworkIn | Inbound Flows | compute.googleapis.com/instance/network/received_packets_count |
| network.sent_throughput | (bytes)| NetworkPacketsOut | Network Out | compute.googleapis.com/instance/network/sent_bytes_count |
| network.sent_pps | (counts)| NetworkOut | Outbound Flows | compute.googleapis.com/instance/network/sent_packets_count |



