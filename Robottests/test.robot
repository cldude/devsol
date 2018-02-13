*** Settings ***
#Documentation   read yaml
#Force Tags      read yaml
Library     ../Honda/Hondacivic.py
#Library    foundation/setupteardown/ClusterMaintenanceSetupTeardown.py
Library     rbtest.py
#Suite Setup    onboard cluster setup
#Suite Teardown    onboard cluster teardown

*** Variables ***
${cluster_name}            "NY-HWI-2-C1"
${verify_type_in_vra}    "onboard-local-cluster"
${verify_type_in_vro}    "onboard-local-cluster"
${a}           2
${b}           3


*** Keywords ***
hello
    log             say hello


*** Test Cases ***
hi
   hello

  #[Documentation]   readyaml
  #[Tags]            readyaml
##  [Setup]           onboard local cluster setup
##  [Teardown]        onboard local cluster teardown
##

###  Check result in vRA    ${verify_type_in_vra}