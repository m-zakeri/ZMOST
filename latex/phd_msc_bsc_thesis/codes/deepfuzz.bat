REM IUST DeepFuzz version 0.2
REM @ECHO off
SET PATH=%PATH%;"C:\Program Files (x86)\Microsoft Visual Studio 14.0\Team Tools\Performance Tools"
CD D:\SUT_DIRECTORY
CLS

START VSPerfMon /coverage /output:fuzzing_code_coverage.coverage
timeout /t 5

FOR %%i IN (.\TEST_DATA\*.pdf) DO ( 
	mupdf %%i
	timeout /t 10
	taskkill /IM mupdf.exe
	timeout /t 2
	)
	
timeout /t 5
VSPerfCmd /shutdown

