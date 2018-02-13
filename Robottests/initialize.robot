*** Settings ***
Documentation   foundation initialize
Force Tags      initialize
Library    common/controller/vCenterCtrl.py
Library    common/controller/vROCtrl.py
Library    common/controller/SQLCtrl.py

*** Variables ***
${snapshotNameofCleanvRO}    cleanvromin
${dbName}    mintj
${fundationPackagePath}    C:\\yuanmin\\installer\\ehc-foundation-4.0.0.0-build-165\\vCO-Workflows\\ehc-foundation-workflows-4.0.0.0-build-165-dev.package
#${fundationPackagePath}    C:\\yuanmin\\fehcci\\ehc-foundation-3.Next.0.0-build-79.zip
${packageType}    Foundation
${foundationInitializeWF}    Initialize EHC Foundation
${dpPackagePath}    C:\\yuanmin\\installer\\ehc-dataProtection-4.0.0.0-build-72\\vCO-Workflows\\ehc-dataProtection-workflows-4.0.0.0-build-72.package
${dpInitializeWF}    Initialize EHC DP
${drPackagePath}    C:\\yuanmin\\installer\\ehc-dr-4.0.0.0-build-54\\vCO-Workflows\\ehc-dr-workflows-4.0.0.0-build-54.package
${drInitializeWF}    Initialize EHC DR



*** Test Cases ***
CI - foundation initialize
  [Documentation]   Given a clean vRO
  ...               And a clean DB
  ...               When I install Fundation package
  ...               And I run Fundation initialize workflow
  ...               Then Fundation initialize workflow complete successfully
  [Tags]            initialize

  Revert vRO to a snapshot    ${snapshotNameofCleanvRO}
  #Delete DB    ${dbName}
  #Create DB    ${dbName}
  Import package    ${packageType}
  Run workflow    ${foundationInitializeWF}
  #Restart vRO Server

#CI - dp initialize
#  [Documentation]   Given foundation is initialized
#  ...               When I install dp package
#  ...               And I run dp initialze workflow
#  ...               Then dp initialize workflow complete successfully
#  [Tags]            initialize
#
#  Import package    ${dpPackagePath}
#  Run workflow    ${dpInitializeWF}
#
#CI - dr initialize
#  [Documentation]   Given foundation is initialized
#  ...               When I install dr package
#  ...               And I run dr initialze workflow
#  ...               Then dr initialize workflow complete successfully
#  [Tags]            initialize
#
#  Import package    ${drPackagePath}
#  Run workflow    ${drInitializeWF}