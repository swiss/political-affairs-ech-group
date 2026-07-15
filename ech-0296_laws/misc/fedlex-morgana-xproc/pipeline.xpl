<p:declare-step xmlns:p="http://www.w3.org/ns/xproc" 
	xmlns:xs="http://www.w3.org/2001/XMLSchema" version="3.1">
            
	<p:output port="result" serialization="map{'indent' : true()}" />
	
	<p:identity>
		<p:with-input>
			<p:inline content-type="text/plain">Hello world. This is an XProc 3.1 pipeline running.</p:inline>
		</p:with-input>
	</p:identity>

</p:declare-step>
