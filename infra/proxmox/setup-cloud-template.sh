#!/usr/bin/env bash
# One-time Proxmox cloud-init template setup script
set -euo pipefail

TEMPLATE_VMID=9000
STORAGE="local-lvm"
BRIDGE="vmbr0"

echo "Downloading Ubuntu 22.04 cloud image..."
wget -q https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img -O /tmp/jammy-cloud.img

echo "Creating VM $TEMPLATE_VMID..."
qm create $TEMPLATE_VMID --name ubuntu-2204-cloud --memory 2048 --cores 2 --net0 virtio,bridge=$BRIDGE

echo "Importing disk image..."
qm importdisk $TEMPLATE_VMID /tmp/jammy-cloud.img $STORAGE

echo "Attaching disk as SCSI..."
qm set $TEMPLATE_VMID --scsihw virtio-scsi-pci --scsi0 $STORAGE:vm-$TEMPLATE_VMID-disk-0

echo "Adding cloud-init drive..."
qm set $TEMPLATE_VMID --ide2 $STORAGE:cloudinit

echo "Setting boot order..."
qm set $TEMPLATE_VMID --boot order=scsi0

echo "Enabling QEMU guest agent..."
qm set $TEMPLATE_VMID --agent enabled=1

echo "Converting to template..."
qm template $TEMPLATE_VMID

echo "Cleaning up..."
rm -f /tmp/jammy-cloud.img

echo "Cloud-init template created successfully (VMID: $TEMPLATE_VMID)"
