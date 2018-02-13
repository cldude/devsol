*** Settings ***
Documentation   cluster maintenance, onboard cluster
Force Tags      cluster maintencae
Library    foundation/controller/ClusterMaintenanceCtrl.py
Library    foundation/setupteardown/ClusterMaintenanceSetupTeardown.py
#Suite Setup    onboard cluster setup
#Suite Teardown    onboard cluster teardown

*** Variables ***
${cluster_name}    "NY-HWI-2-C1"
${verify_type_in_vra}    "onboard-local-cluster"
${verify_type_in_vro}    "onboard-local-cluster"


#*** Test Cases ***
##EHC-3564 - [FD][Cluster Maintenance][Onboard Local Cluster] Onboard local cluster normally
##  [Documentation]   Onboard local cluster
##  [Tags]            onboard local cluster
##  [Setup]           onboard local cluster setup
##  [Teardown]        onboard local cluster teardown
##
##  Onboard local cluster
###  Check result in vRA    ${verify_type_in_vra}
##  Check result in vRO    ${verify_type_in_vro}
