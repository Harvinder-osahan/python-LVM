import os
def Dyp(pvn, vgn, lvn, sz):
    os.system("pvcreate {}".format(pvn))
    os.system("vgcreate {} {}".format(vgn, pvn))
    os.system("lvcreate --size {}G --name {} {}".format(sz, lvn, vgn))
    os.system("lvdisplay /dev/{}/{}".format(vgn, lvn))


def volG(pvn, vgn):
    os.system("vgcreate {} {}".format(vgn, pvn))
    os.system("vgdisplay /dev/{}".format(vgn))


def logiV(vgn, lvn, sz):
    os.system("lvcreate --size {}G --name {} {}".format(sz, lvn, vgn))

def Ext(vgn, lvn, sz):
    os.system("lvextend --size {}G /dev/{}/{}".format(sz, vgn, lvn))

def Red (vgn, lvn, sz):
    os.system("lvreduce -L {}G /dev/{}/{}".format(sz, vgn, lvn))

rep = True

while(rep):
    os.system("tput setaf 3")
    opt = input("[][][] Welcome to logical volume partitioning: \n>>1. Want to create a fresh lvm(pv->vg->lvm). \n>>2. Want to create a new VG \n>>3. Want to create a new LV \n>>4.Add More Vol to LVM \n>>5.Reduce Vol from LVM \n>>6. Delete LV\n>>7. Delete VG\n>>8. Delete PV\n>>9. Exit\n")
    opt = int(opt)
    os.system("tput setaf 6")
    if (opt == 1):
        print("Fresh LVM setup...\n\n")
        pvn = input("PV name(/dev/name): ")
        vgn = input("VG name: ")
        lvn = input("LV name: ")
        sz = input("Size of LVM \n")
        Dyp(pvn, vgn, lvn, int(sz))
        print("Done!!")

    elif (opt == 2):
        print("New VG")
        pvn = input("PV name: ")
        vgn = input("VG name: ")
        volG(pvn, vgn)
        print("\nDone!!")

    elif (opt == 3):
        print("New LV")
        vgn = input("VG name(which is already created): ")
        lvn = input("LV name : ")
        sz = input("Size of LV in GiB")
        logiV(vgn, lvn,int(sz))
        print("\nDone!!")

    elif (opt == 4):
        print("Extend LVM")
        vgn = input("VG name: ")
        lvn = input("LV name: ")
        sz = input("Size in GiB. which you want to extend: ")
        Ext(vgn,lvn, int(sz))
        print("\nDone!!")

    elif (opt == 5):
        print("Reduce LVM")
        vgn = input("VG name: ")
        lvn = input("LV name: ")
        sz = input("Size in GiB. which you want to reduce: ")
        Red(vgn,lvn, int(sz))
        print("\nDone!!")
    elif (opt == 6):
        print("Remove LV")
        vgn = input("VG name: ")
        lvn = input("LV name: ")
        os.system("lvremove -f /dev/{}/{}".format(vgn, lvn))

    elif (opt == 7):
        print("Remove VG")
        vgn = input("VG name: ")
        os.system("vgremove /dev/{}".format(vgn))

    elif (opt == 8):
        print("Remove PV")
        pvn = input("pvname: ")
        os.system("pvremove {}".format(pvn))

    elif (opt ==9):
        os.system("tput setaf 7")
        exit()

    ch = input("Want to do something else: y/n")
    if ch == 'y':
        rep = True
    else:
        rep = False

os.system("tput setaf 7")
