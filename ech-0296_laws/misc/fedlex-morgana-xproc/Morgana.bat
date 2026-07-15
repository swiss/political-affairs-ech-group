@echo off
setlocal

set MORGANADIR=%~dp0

REM All related jars are expected to be in $MORGANA_LIB. For externals jars: Add them to $CLASSPATH
set PROG_PATH="%MORGANADIR%MorganaXProc-IIIse.jar"
set LIB_PATH="%MORGANADIR%MorganaXProc-IIIse_lib/*"

set CLASSPATH="%LIB_PATH%;%PROG_PATH%"

REM Settings for JAVA_AGENT: Only for Java 8 we have to use -javaagent.
@for /f tokens^=2-5^ delims^=.-_^" %%j in ('java -fullversion 2^>^&1') do set "JAVA_VERSION=%%j%%k"

set JAVA_AGENT=
if %JAVA_VERSION% EQU 18 (set JAVA_AGENT="-javaagent:%MORGANADIR%MorganaXProc-IIIse_lib/quasar-core-0.7.9.jar")

java %JAVA_AGENT% -cp %CLASSPATH% com.xml_project.morganaxproc3.XProcEngine %*
REM Alternative if you encounter instrumentation errors using Java 8
REM java -cp %CLASSPATH% com.xml_project.morganaxproc3.XProcEngine %* -mopl-mode=linear