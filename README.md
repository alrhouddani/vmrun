## Prerequisites
> Python3 and above
> Vmware Player or workstation 
> Vmrum.exe 
> Variables Must be declared
- vmrun.VMware_path = "Vmware Player application Path"
- vmrun.OVFTool = "OVFTool Path"
- vmrun.vms_path = "vmx Path vmx"

## Introduction
> About The Module
This is a Python Module That allows you to manage all your Vmware Vms using Python 

## Start Vms
```
vm = "\Virtual Machines\Centos-server\Centos-server.vmx" 
vmrun.start(vm)
```
## Stop Vms
```
vm = "\Virtual Machines\Centos-server\Centos-server.vmx" 
vmrun.stop(vm)
```
## Restart Vms
```
vm = "\Virtual Machines\Centos-server\Centos-server.vmx" 
vmrun.restart(vm)
```
## list Runing Vms
```
vmrun.list()
```
## Export Vms
```
vmname = "Centos-server" 
vmrun.export(vmname)
```
## Compact Disk
```
vmname = "Centos-server" 
vmrun.Compact(vmname)
```
## Defrag Disk
```
vmname = "Centos-server" 
vmrun.Defrag(vmname)
```
## Repair Disk
```
vmname = "Centos-server" 
vmrun.Repair(vmname)
```
## runProgramInGuest
```
user = "Admin"
vmname = "Centos-server" 
program = "firefox.exe
runProgramInGuest(user, vmname, program)
```
