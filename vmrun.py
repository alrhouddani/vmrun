
import os
import subprocess
from getpass import getpass

VMware_path = ""
OVFTool = ""
vms_path = ""
vdiskmanager = ""


def start(vmname):
    os.chdir(VMware_path)
    cmd = f"./vmrun start '{vms_path}\{vmname}\{vmname}.vmx' nogui"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"Successfully Started The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def stop(vmname):
    os.chdir(VMware_path)
    cmd = f"./vmrun stop '{vms_path}\{vmname}\{vmname}.vmx'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"Successfully Stopped The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def export(vmname, ovfname):
    os.chdir(OVFTool)
    cmd = f"./ovftool '{vms_path}{vmname}\\{vmname}.vmx' '{vms_path}\Export\\{ovfname}.ovf'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"Successfully Exported The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    print(completed.stdout)
    return completed

# create_snap


def create_snap(vmname, snapname):
    vmplayer = "Stop-Process -Name vmplayer -Force -Confirm:$false -ErrorAction Ignore"
    subprocess.run(
        ["powershell", "-Command", vmplayer], capture_output=True)
    os.chdir(VMware_path)
    cmd = f"./vmrun -T ws snapshot '{vms_path}\{vmname}\{vmname}.vmx' {snapname}"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(
            f"Successfully Created a Snapshot of The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed

# list snapshots


def listSnapshots(vmname):
    os.chdir(VMware_path)
    cmd = f"./vmrun -T ws listSnapshots '{vms_path}\{vmname}\{vmname}.vmx'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"{vmname} Snapshots {completed.stdout}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed

# delete Snapshot


def deleteSnapshot(vmname, snapname):
    os.chdir(VMware_path)
    cmd = f"./vmrun -T ws deleteSnapshot '{vms_path}\{vmname}\{vmname}.vmx' '{snapname}'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"{completed.stdout}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def revertToSnapshot(vmname, snapname):
    os.chdir(VMware_path)
    cmd = f"./vmrun -T ws revertToSnapshot '{vms_path}\{vmname}\{vmname}.vmx' '{snapname}'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"{completed.stdout}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def list():
    os.chdir(VMware_path)
    cmd = "./vmrun list"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    print(completed.stdout)
    if completed.returncode == 1:
        print(f"Script run with issue Please check your {VMware_path}")


def restart(vmname):
    os.chdir(VMware_path)
    cmd = f"./vmrun reset '{vms_path}{vmname}\\{vmname}.vmx'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(f"Successfully Restarted The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def copyFileToGuest(user, vmname, src, dest):
    Guestpassword = getpass()
    os.chdir(VMware_path)
    cmd = f".//vmrun -T ws -gu {user} -gp {Guestpassword} copyFileFromHostToGuest '{vms_path}{vmname}\\{vmname}.vmx' {src} {dest}"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(
            f"Successfully Transferred The File To The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def runProgramInGuest(user, vmname, program):
    Guestpassword = getpass()
    os.chdir(VMware_path)
    cmd = f".//vmrun -T ws -gu {user} -gp {Guestpassword} runProgramInGuest '{vms_path}{vmname}\\{vmname}.vmx' -activeWindow '{program}'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(
            f"Successfully Ran The Program On The Virtual Machine {vmname}")
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def compact(vmname):
    os.chdir(vdiskmanager)
    cmd = f".\\vmware-vdiskmanager.exe -k '{vms_path}\{vmname}\{vmname}.vmdk'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(completed.stderr)
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def Defrag(vmname):
    os.chdir(vdiskmanager)
    cmd = f".\\vmware-vdiskmanager.exe -d '{vms_path}\{vmname}\{vmname}.vmdk'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(completed.stderr)
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed


def repair(vmname):
    os.chdir(vdiskmanager)
    cmd = f".\\vmware-vdiskmanager.exe -R '{vms_path}\{vmname}\{vmname}.vmdk'"
    completed = subprocess.run(
        ["powershell", "-Command", cmd], capture_output=True)
    if completed.returncode == 0:
        print(completed.stderr)
    elif completed.returncode == 1:
        print(f"Script run with issue Please check your {vmname}")
    return completed
