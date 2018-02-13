*** Settings ***
Documentation   cluster maintenance, onboard cluster
Force Tags      cluster maintencae
Library    foundation/controller/ClusterMaintenanceCtrl.py
Library    foundation/setupteardown/ClusterMaintenanceSetupTeardown.py
#Suite Setup    hardware island maintenance setup
#Suite Teardown    hardware island maintenance teardown

*** Variables ***
${verify_type_in_vra}    "add-hardware-island"
${verify_type_in_vro}    "add-hardware-island"


*** Test Cases ***
#EHC-3303 - [FD][Hardware Island Maintenance] Add a new Hardware Island
#  [Documentation]   Onboard local cluster
#  [Tags]            onboard local cluster
#  [Setup]           onboard local cluster setup
#  [Teardown]        onboard local cluster teardown
#
#  Onboard local cluster
##  Check result in vRA    ${verify_type_in_vra}
#  Check result in vRO    ${verify_type_in_vro}