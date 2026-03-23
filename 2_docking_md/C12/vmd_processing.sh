#!/usr/bin/bash


################################################################################
#  This bash script processes MD simulations generated with the                #
# desmond_slurm.sh script. Job settings need to match the ones from the        #
# desmond_slurm.sh script. The protein will be centered in the water box using #
# the pbc wrap tool and the protein will be aligned on the backbone heavy      #
# atoms of the first frame. The processed data will be saved as pdb and dcd    #
# file in a directory called mds_prep.                                         #
################################################################################

# @author david schaller

# job settings
REPLICA=5
NAME=desmond_md_job_1

# path to vmd executable
VMD=/software/vmd/vmd-1.9.3/vmd

# create tcl-file for vmd conversion
echo "Creating temporary vmd conversion file ..."
if [ -f md_conversion.tcl ]; then
  rm md_conversion.tcl
fi
cat > md_conversion.tcl << EOF
package require pbctools
pbc wrap -centersel protein -center com -compound res -all
proc fitframes { molid seltext } {
  set ref [atomselect \$molid \$seltext frame 0]
  set sel [atomselect \$molid \$seltext]
  set all [atomselect \$molid all]
  set n [molinfo \$molid get numframes]

  for { set i 1 } { \$i < \$n } { incr i } {
    \$sel frame \$i
    \$all frame \$i
    \$all move [measure fit \$sel \$ref]
  }
  return
}
fitframes top backbone
animate write pdb mds_prep/\$argv.pdb beg 0 end 0
animate write dcd mds_prep/\$argv.dcd beg 1 end 1001
quit
EOF

# make directory
if [ ! -d mds_prep ]; then
  mkdir mds_prep
fi

for counter in $(seq 0 $((REPLICA - 1)))
do
  ${VMD} \
    -f ${counter}/${NAME}_${counter}-in.cms ${counter}/${NAME}_${counter}_trj/clickme.dtr \
    -dispdev text \
    -e md_conversion.tcl \
    -eofexit \
    -args ${counter}
done

# remove temporary vmd conversion script
rm md_conversion.tcl
