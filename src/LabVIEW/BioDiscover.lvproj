<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="20008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">false</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="IOScan.Faults" Type="Str"></Property>
		<Property Name="IOScan.NetVarPeriod" Type="UInt">100</Property>
		<Property Name="IOScan.NetWatchdogEnabled" Type="Bool">false</Property>
		<Property Name="IOScan.Period" Type="UInt">10000</Property>
		<Property Name="IOScan.PowerupMode" Type="UInt">0</Property>
		<Property Name="IOScan.Priority" Type="UInt">9</Property>
		<Property Name="IOScan.ReportModeConflict" Type="Bool">true</Property>
		<Property Name="IOScan.StartEngineOnDeploy" Type="Bool">false</Property>
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Type Definitions" Type="Folder">
			<Item Name="Data.ctl" Type="VI" URL="../controls/Data.ctl"/>
			<Item Name="State.ctl" Type="VI" URL="../controls/State.ctl"/>
			<Item Name="Camera_ID.ctl" Type="VI" URL="../Camera_ID.ctl"/>
			<Item Name="Image_Data.ctl" Type="VI" URL="../controls/Image_Data.ctl"/>
		</Item>
		<Item Name="Controls" Type="Folder">
			<Item Name="Terminate_Pump.ctl" Type="VI" URL="../controls/Terminate_Pump.ctl"/>
			<Item Name="Stop_Program.ctl" Type="VI" URL="../controls/Stop_Program.ctl"/>
		</Item>
		<Item Name="src" Type="Folder">
			<Item Name="Camera" Type="Folder">
				<Item Name="Image Acquisition" Type="Folder">
					<Item Name="Image_Snap_Enqueue.vi" Type="VI" URL="../Image_Snap_Enqueue.vi"/>
					<Item Name="Image_Snap_Dual.vi" Type="VI" URL="../Image_Snap_Dual.vi"/>
					<Item Name="Image_Acquisition_Stop.vi" Type="VI" URL="../Image_Acquisition_Stop.vi"/>
					<Item Name="Image_Snap_Single.vi" Type="VI" URL="../Image_Snap_Single.vi"/>
				</Item>
				<Item Name="Camera_ID.vi" Type="VI" URL="../Camera_ID.vi"/>
				<Item Name="Camera_init.vi" Type="VI" URL="../Camera_init.vi"/>
				<Item Name="Camera_Config.vi" Type="VI" URL="../Camera_Config.vi"/>
				<Item Name="Camera_Capture_Init.vi" Type="VI" URL="../Camera_Capture_Init.vi"/>
				<Item Name="Capture_Save_Initialize.vi" Type="VI" URL="../Capture_Save_Initialize.vi"/>
				<Item Name="Camera_Crop_Setup.vi" Type="VI" URL="../Camera_Crop_Setup.vi"/>
				<Item Name="Camera_Crop_Decluster.vi" Type="VI" URL="../Camera_Crop_Decluster.vi"/>
			</Item>
			<Item Name="Pump and Actuator" Type="Folder">
				<Item Name="Init_XE1000Pump.vi" Type="VI" URL="../Init_XE1000Pump.vi"/>
				<Item Name="Init_L16LinearActuator.vi" Type="VI" URL="../Init_L16LinearActuator.vi"/>
				<Item Name="ID_Connection.vi" Type="VI" URL="../ID_Connection.vi"/>
				<Item Name="Empty_Complete.vi" Type="VI" URL="../Empty_Complete.vi"/>
			</Item>
			<Item Name="Images" Type="Folder">
				<Item Name="Save" Type="Folder">
					<Item Name="Image_Folder.vi" Type="VI" URL="../Image_Folder.vi"/>
					<Item Name="Image_Save.vi" Type="VI" URL="../Image_Save.vi"/>
					<Item Name="Folder_Create.vi" Type="VI" URL="../Folder_Create.vi"/>
					<Item Name="Image_Save_Dequeue.vi" Type="VI" URL="../Image_Save_Dequeue.vi"/>
					<Item Name="Image_Save_Handler.vi" Type="VI" URL="../Image_Save_Handler.vi"/>
				</Item>
				<Item Name="Detect and Crop" Type="Folder">
					<Item Name="Image_Handler.vi" Type="VI" URL="../Image_Handler.vi"/>
					<Item Name="Image_Crop_to_Object.vi" Type="VI" URL="../Image_Crop_to_Object.vi"/>
					<Item Name="Image_Detect_Object.vi" Type="VI" URL="../Image_Detect_Object.vi"/>
					<Item Name="Image_Crop_Fixed.vi" Type="VI" URL="../Image_Crop_Fixed.vi"/>
					<Item Name="Image_Crop_Fixed_Area.vi" Type="VI" URL="../Image_Crop_Fixed_Area.vi"/>
					<Item Name="Image_Processing_Queue.vi" Type="VI" URL="../Image_Processing_Queue.vi"/>
					<Item Name="Image_Processing_Queue_Info.vi" Type="VI" URL="../Image_Processing_Queue_Info.vi"/>
				</Item>
			</Item>
			<Item Name="System" Type="Folder">
				<Item Name="Terminate_Connection.vi" Type="VI" URL="../Terminate_Connection.vi"/>
				<Item Name="Connections.vi" Type="VI" URL="../Connections.vi"/>
				<Item Name="Settings_Load.vi" Type="VI" URL="../Settings_Load.vi"/>
				<Item Name="Settings_Save.vi" Type="VI" URL="../Settings_Save.vi"/>
				<Item Name="Save_File_Sample_Setup.vi" Type="VI" URL="../Save_File_Sample_Setup.vi"/>
				<Item Name="Disable Keys.vi" Type="VI" URL="../Disable Keys.vi"/>
				<Item Name="Enable Keys.vi" Type="VI" URL="../Enable Keys.vi"/>
			</Item>
			<Item Name="Calibration" Type="Folder">
				<Item Name="Calibration_Folder.vi" Type="VI" URL="../Calibration_Folder.vi"/>
				<Item Name="Calibration_Capture.vi" Type="VI" URL="../Calibration_Capture.vi"/>
				<Item Name="Calibration_Update.vi" Type="VI" URL="../Calibration_Update.vi"/>
				<Item Name="Calibration_Save.vi" Type="VI" URL="../Calibration_Save.vi"/>
				<Item Name="Calibration_Load.vi" Type="VI" URL="../Calibration_Load.vi"/>
				<Item Name="Calibration_Setup_file.vi" Type="VI" URL="../Calibration_Setup_file.vi"/>
				<Item Name="Calibration_Quadruple_Save.vi" Type="VI" URL="../Calibration_Quadruple_Save.vi"/>
			</Item>
			<Item Name="Data Files" Type="Folder">
				<Item Name="CSV_Setup_Data_Create.vi" Type="VI" URL="../CSV_Setup_Data_Create.vi"/>
				<Item Name="CSV_Setup_Data_Handler.vi" Type="VI" URL="../CSV_Setup_Data_Handler.vi"/>
				<Item Name="CSV_Setup_Data_Append.vi" Type="VI" URL="../CSV_Setup_Data_Append.vi"/>
				<Item Name="Sample_Data_Compute.vi" Type="VI" URL="../Sample_Data_Compute.vi"/>
				<Item Name="Sample_Data_Subset.vi" Type="VI" URL="../Sample_Data_Subset.vi"/>
				<Item Name="Save_Folder_Path.vi" Type="VI" URL="../Save_Folder_Path.vi"/>
				<Item Name="CSV_Image_Data_Append.vi" Type="VI" URL="../CSV_Image_Data_Append.vi"/>
				<Item Name="CSV_Image_Data_Create.vi" Type="VI" URL="../CSV_Image_Data_Create.vi"/>
			</Item>
			<Item Name="Timestamp.vi" Type="VI" URL="../Timestamp.vi"/>
			<Item Name="Save_Truth_Table.vi" Type="VI" URL="../Save_Truth_Table.vi"/>
		</Item>
		<Item Name="Test Functions" Type="Folder">
			<Item Name="CameraStream.vi" Type="VI" URL="../CameraStream.vi"/>
			<Item Name="CameraStreamIMAQ.vi" Type="VI" URL="../CameraStreamIMAQ.vi"/>
			<Item Name="CameraStreamAttribute.vi" Type="VI" URL="../CameraStreamAttribute.vi"/>
			<Item Name="Camera_Reconfig.vi" Type="VI" URL="../Camera_Reconfig.vi"/>
			<Item Name="CameraAttributeSearch.vi" Type="VI" URL="../CameraAttributeSearch.vi"/>
			<Item Name="CameraAttributeTest.vi" Type="VI" URL="../CameraAttributeTest.vi"/>
			<Item Name="USBInterfaceFetch.vi" Type="VI" URL="../USBInterfaceFetch.vi"/>
			<Item Name="Arduino_Communication.vi" Type="VI" URL="../Arduino_Communication.vi"/>
			<Item Name="Enqueue_Acquisition.vi" Type="VI" URL="../Enqueue_Acquisition.vi"/>
			<Item Name="CSV_Setup_Data.vi" Type="VI" URL="../CSV_Setup_Data.vi"/>
			<Item Name="Pump_Status.vi" Type="VI" URL="../Pump_Status.vi"/>
			<Item Name="CameraSerialIDScan.vi" Type="VI" URL="../CameraSerialIDScan.vi"/>
			<Item Name="Bayer12bit.vi" Type="VI" URL="../Bayer12bit.vi"/>
		</Item>
		<Item Name="resources" Type="Folder">
			<Item Name="Icon.ico" Type="Document" URL="../resources/Icon.ico"/>
		</Item>
		<Item Name="Main.vi" Type="VI" URL="../Main.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="NI_Vision_Acquisition_Software.lvlib" Type="Library" URL="/&lt;vilib&gt;/vision/driver/NI_Vision_Acquisition_Software.lvlib"/>
				<Item Name="IMAQdx.ctl" Type="VI" URL="/&lt;vilib&gt;/userDefined/High Color/IMAQdx.ctl"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Create"/>
				<Item Name="IMAQ Dispose" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Dispose"/>
				<Item Name="IMAQ Write TIFF File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write TIFF File 2"/>
				<Item Name="IMAQ Write PNG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write PNG File 2"/>
				<Item Name="IMAQ Write JPEG2000 File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG2000 File 2"/>
				<Item Name="IMAQ Write JPEG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG File 2"/>
				<Item Name="IMAQ Write Image And Vision Info File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write Image And Vision Info File 2"/>
				<Item Name="IMAQ Write BMP File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write BMP File 2"/>
				<Item Name="IMAQ Write File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write File 2"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="ROI Descriptor" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/ROI Descriptor"/>
				<Item Name="NI_Vision_Development_Module.lvlib" Type="Library" URL="/&lt;vilib&gt;/vision/NI_Vision_Development_Module.lvlib"/>
				<Item Name="IVA Mask from ROI.vi" Type="VI" URL="/&lt;vilib&gt;/vision/Vision Assistant Utils.llb/IVA Mask from ROI.vi"/>
				<Item Name="Particle Parameters" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Particle Parameters"/>
				<Item Name="Stall Data Flow.vim" Type="VI" URL="/&lt;vilib&gt;/Utility/Stall Data Flow.vim"/>
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="compatCalcOffset.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatCalcOffset.vi"/>
				<Item Name="compatOpenFileOperation.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOpenFileOperation.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="Open_Create_Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/Open_Create_Replace File.vi"/>
				<Item Name="Write to XML File(array).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Write to XML File(array).vi"/>
				<Item Name="Write to XML File(string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Write to XML File(string).vi"/>
				<Item Name="Write to XML File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Write to XML File.vi"/>
				<Item Name="FindElementStartByName.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindElementStartByName.vi"/>
				<Item Name="FindCloseTagByName.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindCloseTagByName.vi"/>
				<Item Name="FindMatchingCloseTag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindMatchingCloseTag.vi"/>
				<Item Name="FindElement.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindElement.vi"/>
				<Item Name="FindEmptyElement.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindEmptyElement.vi"/>
				<Item Name="FindFirstTag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/FindFirstTag.vi"/>
				<Item Name="ParseXMLFragments.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/ParseXMLFragments.vi"/>
				<Item Name="Read From XML File(string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Read From XML File(string).vi"/>
				<Item Name="Read From XML File(array).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Read From XML File(array).vi"/>
				<Item Name="Read From XML File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/xml.llb/Read From XML File.vi"/>
				<Item Name="VISA Find Search Mode.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Find Search Mode.ctl"/>
				<Item Name="Color (U64)" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Color (U64)"/>
				<Item Name="IMAQ ColorImageToArray" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ ColorImageToArray"/>
				<Item Name="IMAQ ArrayToColorImage" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ ArrayToColorImage"/>
				<Item Name="IMAQ GetImageSize" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ GetImageSize"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="IMAQ ReadFile 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ ReadFile 2"/>
				<Item Name="IMAQ Rectangle" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Rectangle"/>
				<Item Name="IMAQ WindEraseROI" Type="VI" URL="/&lt;vilib&gt;/vision/ROI Display.llb/IMAQ WindEraseROI"/>
				<Item Name="IMAQ Convert ROI to Rectangle" Type="VI" URL="/&lt;vilib&gt;/vision/ROI Conversion.llb/IMAQ Convert ROI to Rectangle"/>
				<Item Name="IMAQ ConstructROI" Type="VI" URL="/&lt;vilib&gt;/vision/ROI Display.llb/IMAQ ConstructROI"/>
				<Item Name="IMAQ Select Rectangle" Type="VI" URL="/&lt;vilib&gt;/vision/ROI Construct.llb/IMAQ Select Rectangle"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="IMAQ Bayer To RGB" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Bayer To RGB"/>
				<Item Name="IMAQ Image Bit Depth" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Image Bit Depth"/>
				<Item Name="IMAQ ImageToArray" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ ImageToArray"/>
				<Item Name="IMAQ ArrayToImage" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ ArrayToImage"/>
				<Item Name="imgUpdateErrorCluster.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgUpdateErrorCluster.vi"/>
				<Item Name="imgClose.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgClose.vi"/>
				<Item Name="IMAQRegisterSession.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/IMAQRegisterSession.vi"/>
				<Item Name="imgSessionOpen.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgSessionOpen.vi"/>
				<Item Name="imgInterfaceOpen.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgInterfaceOpen.vi"/>
				<Item Name="IMAQ Init.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/imaqhl.llb/IMAQ Init.vi"/>
				<Item Name="SessionLookUp.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/SessionLookUp.vi"/>
				<Item Name="imgSetGetRoiInternal.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgSetGetRoiInternal.vi"/>
				<Item Name="imgPopScalingAndROI.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgPopScalingAndROI.vi"/>
				<Item Name="imgPopScalingAndROIWhenFinished.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgPopScalingAndROIWhenFinished.vi"/>
				<Item Name="imgAssociateBufListWithInterface.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgAssociateBufListWithInterface.vi"/>
				<Item Name="IMAQ Attribute.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/imaqhl.llb/IMAQ Attribute.vi"/>
				<Item Name="imgGrabSetup.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgGrabSetup.vi"/>
				<Item Name="imgSetRoi.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgSetRoi.vi"/>
				<Item Name="imgSetGetScaling.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgSetGetScaling.vi"/>
				<Item Name="imgSetChannel.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgSetChannel.vi"/>
				<Item Name="imgPushScalingAndROI.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgPushScalingAndROI.vi"/>
				<Item Name="IMAQ Grab Setup.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/imaqhl.llb/IMAQ Grab Setup.vi"/>
				<Item Name="IMAQ GetImagePixelPtr" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ GetImagePixelPtr"/>
				<Item Name="imgGrabArea.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgGrabArea.vi"/>
				<Item Name="IMAQ Image Cluster to Image Datatype.vi" Type="VI" URL="/&lt;vilib&gt;/vision/DatatypeConversion.llb/IMAQ Image Cluster to Image Datatype.vi"/>
				<Item Name="IMAQ Image Datatype to Image Cluster.vi" Type="VI" URL="/&lt;vilib&gt;/vision/DatatypeConversion.llb/IMAQ Image Datatype to Image Cluster.vi"/>
				<Item Name="imgGetBitsPerComponent.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgGetBitsPerComponent.vi"/>
				<Item Name="imgReconstructimage.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgReconstructimage.vi"/>
				<Item Name="IMAQ Grab Acquire Old Style.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/IMAQ Grab Acquire Old Style.vi"/>
				<Item Name="imgIsNewStyleInterface.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/imgIsNewStyleInterface.vi"/>
				<Item Name="IMAQ Grab Acquire.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/imaqhl.llb/IMAQ Grab Acquire.vi"/>
				<Item Name="IMAQUnregisterSession.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/DLLCalls.llb/IMAQUnregisterSession.vi"/>
				<Item Name="IMAQ Close.vi" Type="VI" URL="/&lt;vilib&gt;/vision/driver/imaqhl.llb/IMAQ Close.vi"/>
				<Item Name="IMAQ Copy" Type="VI" URL="/&lt;vilib&gt;/vision/Management.llb/IMAQ Copy"/>
			</Item>
			<Item Name="niimaqdx.dll" Type="Document" URL="niimaqdx.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivision.dll" Type="Document" URL="nivision.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Tag-c(bool,bool).lvlib" Type="Library" URL="/&lt;extravilib&gt;/ChannelInstances/Tag-c(bool,bool).lvlib"/>
			<Item Name="_ChannelSupport.lvlib" Type="Library" URL="/&lt;resource&gt;/ChannelSupport/_ChannelSupport/_ChannelSupport.lvlib"/>
			<Item Name="Tag-t&apos;Data.ctl&apos;.lvlib" Type="Library" URL="/&lt;extravilib&gt;/ChannelInstances/Tag-t&apos;Data.ctl&apos;.lvlib"/>
			<Item Name="Tag-bool.lvlib" Type="Library" URL="/&lt;extravilib&gt;/ChannelInstances/Tag-bool.lvlib"/>
			<Item Name="ChannelProbePositionAndTitle.vi" Type="VI" URL="/&lt;resource&gt;/ChannelSupport/_ChannelSupport/ChannelProbePositionAndTitle.vi"/>
			<Item Name="ChannelProbeWindowStagger.vi" Type="VI" URL="/&lt;resource&gt;/ChannelSupport/_ChannelSupport/ChannelProbeWindowStagger.vi"/>
			<Item Name="imaq.dll" Type="Document" URL="imaq.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="SRS" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{B511CD8F-BE21-4470-A7C4-3ACBADFC72C8}</Property>
				<Property Name="App_INI_GUID" Type="Str">{78EABFCD-5B97-4F87-AF3F-FF129EE73305}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">1</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{2CE40C4E-446A-4350-9E11-C85D8BAE8F13}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">SRS</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/C/Users/au540322/Documents/Projects/NI_AB_PROJECTNAME/Builds/Full Build</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{09FD23A0-93D2-46A2-B12D-FA02255F97C6}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Bld_version.minor" Type="Int">5</Property>
				<Property Name="Destination[0].destName" Type="Str">SRS.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/C/Users/au540322/Documents/Projects/NI_AB_PROJECTNAME/Builds/Full Build/SRS.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">/C/Users/au540322/Documents/Projects/NI_AB_PROJECTNAME/Builds/Full Build/data</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Exe_iconItemID" Type="Ref">/My Computer/resources/Icon.ico</Property>
				<Property Name="Source[0].itemID" Type="Str">{B6041F0C-7AFF-4CAC-AADE-763442917E0A}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Main.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Show toolbar</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[1].type" Type="Str">Show menu bar</Property>
				<Property Name="Source[1].properties[1].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">2</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/src</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/Controls</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[4].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/Type Definitions</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[4].type" Type="Str">Container</Property>
				<Property Name="SourceCount" Type="Int">5</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Species Recognition System</Property>
				<Property Name="TgtF_internalName" Type="Str">SRS</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2012 </Property>
				<Property Name="TgtF_productName" Type="Str">SRS</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{A9B9C488-ADD7-40F6-AAC2-547427E5CB24}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">SRS.exe</Property>
			</Item>
			<Item Name="SRS Installer" Type="Installer">
				<Property Name="Destination[0].name" Type="Str">SRS</Property>
				<Property Name="Destination[0].parent" Type="Str">{3912416A-D2E5-411B-AFEE-B63654D690C0}</Property>
				<Property Name="Destination[0].tag" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Destination[0].type" Type="Str">userFolder</Property>
				<Property Name="Destination[0].unlock" Type="Bool">true</Property>
				<Property Name="DestinationCount" Type="Int">1</Property>
				<Property Name="DistPart[0].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[0].productID" Type="Str">{57C41B25-A232-4945-B942-D7EC8ECBE6EF}</Property>
				<Property Name="DistPart[0].productName" Type="Str">NI Vision Common Resources 2020</Property>
				<Property Name="DistPart[0].upgradeCode" Type="Str">{409BEFA9-EB3E-472F-AD77-271A4A1D5927}</Property>
				<Property Name="DistPart[1].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[1].productID" Type="Str">{633A1550-642D-4DAB-A449-234FEFC53097}</Property>
				<Property Name="DistPart[1].productName" Type="Str">NI Vision Runtime 2020</Property>
				<Property Name="DistPart[1].upgradeCode" Type="Str">{63DF74E5-A5C9-11D4-814E-005004D6CDD6}</Property>
				<Property Name="DistPart[2].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[2].productID" Type="Str">{CB6C2533-4926-42B8-AC21-04BB9679F818}</Property>
				<Property Name="DistPart[2].productName" Type="Str">NI-488.2 Runtime 20.0</Property>
				<Property Name="DistPart[2].upgradeCode" Type="Str">{357F6618-C660-41A2-A185-5578CC876D1D}</Property>
				<Property Name="DistPart[3].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[3].productID" Type="Str">{2A34BA62-42F5-4FA3-BE08-862AC6C2F628}</Property>
				<Property Name="DistPart[3].productName" Type="Str">NI-IMAQdx Runtime 20.0</Property>
				<Property Name="DistPart[3].upgradeCode" Type="Str">{3D104AB3-CE10-43C0-B647-07600754072C}</Property>
				<Property Name="DistPart[4].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[4].productID" Type="Str">{F12C6F92-5B1C-4EAB-9364-96026CE1920D}</Property>
				<Property Name="DistPart[4].productName" Type="Str">NI-Serial Runtime 20.0</Property>
				<Property Name="DistPart[4].upgradeCode" Type="Str">{01D82F43-B48D-46FF-8601-FC4FAAE20F41}</Property>
				<Property Name="DistPart[5].flavorID" Type="Str">_deployment_</Property>
				<Property Name="DistPart[5].productID" Type="Str">{944CC86F-BDFB-4850-878C-370B9A7FF12C}</Property>
				<Property Name="DistPart[5].productName" Type="Str">NI-VISA Runtime 20.0</Property>
				<Property Name="DistPart[5].upgradeCode" Type="Str">{8627993A-3F66-483C-A562-0D3BA3F267B1}</Property>
				<Property Name="DistPart[6].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[6].productID" Type="Str">{CED05116-2329-4D0D-92CA-CEC520182EB0}</Property>
				<Property Name="DistPart[6].productName" Type="Str">NI LabVIEW Runtime 2020 f1</Property>
				<Property Name="DistPart[6].SoftDep[0].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[0].productName" Type="Str">NI ActiveX Container</Property>
				<Property Name="DistPart[6].SoftDep[0].upgradeCode" Type="Str">{1038A887-23E1-4289-B0BD-0C4B83C6BA21}</Property>
				<Property Name="DistPart[6].SoftDep[1].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[1].productName" Type="Str">NI Deployment Framework 2020</Property>
				<Property Name="DistPart[6].SoftDep[1].upgradeCode" Type="Str">{838942E4-B73C-492E-81A3-AA1E291FD0DC}</Property>
				<Property Name="DistPart[6].SoftDep[10].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[10].productName" Type="Str">NI VC2015 Runtime</Property>
				<Property Name="DistPart[6].SoftDep[10].upgradeCode" Type="Str">{D42E7BAE-6589-4570-B6A3-3E28889392E7}</Property>
				<Property Name="DistPart[6].SoftDep[11].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[11].productName" Type="Str">NI TDM Streaming 19.0</Property>
				<Property Name="DistPart[6].SoftDep[11].upgradeCode" Type="Str">{4CD11BE6-6BB7-4082-8A27-C13771BC309B}</Property>
				<Property Name="DistPart[6].SoftDep[2].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[2].productName" Type="Str">NI Error Reporting 2020</Property>
				<Property Name="DistPart[6].SoftDep[2].upgradeCode" Type="Str">{42E818C6-2B08-4DE7-BD91-B0FD704C119A}</Property>
				<Property Name="DistPart[6].SoftDep[3].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[3].productName" Type="Str">NI LabVIEW Real-Time NBFifo 2020</Property>
				<Property Name="DistPart[6].SoftDep[3].upgradeCode" Type="Str">{00D0B680-F876-4E42-A25F-52B65418C2A6}</Property>
				<Property Name="DistPart[6].SoftDep[4].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[4].productName" Type="Str">NI LabVIEW Runtime 2020 Non-English Support.</Property>
				<Property Name="DistPart[6].SoftDep[4].upgradeCode" Type="Str">{61FCC73D-8092-457D-8905-27C0060D88E1}</Property>
				<Property Name="DistPart[6].SoftDep[5].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[5].productName" Type="Str">NI Logos 20.0</Property>
				<Property Name="DistPart[6].SoftDep[5].upgradeCode" Type="Str">{5E4A4CE3-4D06-11D4-8B22-006008C16337}</Property>
				<Property Name="DistPart[6].SoftDep[6].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[6].productName" Type="Str">NI LabVIEW Web Server 2020</Property>
				<Property Name="DistPart[6].SoftDep[6].upgradeCode" Type="Str">{0960380B-EA86-4E0C-8B57-14CD8CCF2C15}</Property>
				<Property Name="DistPart[6].SoftDep[7].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[7].productName" Type="Str">NI mDNS Responder 19.0</Property>
				<Property Name="DistPart[6].SoftDep[7].upgradeCode" Type="Str">{9607874B-4BB3-42CB-B450-A2F5EF60BA3B}</Property>
				<Property Name="DistPart[6].SoftDep[8].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[8].productName" Type="Str">Math Kernel Libraries 2017</Property>
				<Property Name="DistPart[6].SoftDep[8].upgradeCode" Type="Str">{699C1AC5-2CF2-4745-9674-B19536EBA8A3}</Property>
				<Property Name="DistPart[6].SoftDep[9].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[9].productName" Type="Str">Math Kernel Libraries 2020</Property>
				<Property Name="DistPart[6].SoftDep[9].upgradeCode" Type="Str">{9872BBBA-FB96-42A4-80A2-9605AC5CBCF1}</Property>
				<Property Name="DistPart[6].SoftDepCount" Type="Int">12</Property>
				<Property Name="DistPart[6].upgradeCode" Type="Str">{D84FC73F-D1E0-4C05-A30C-DB882CD1ABD8}</Property>
				<Property Name="DistPartCount" Type="Int">7</Property>
				<Property Name="INST_author" Type="Str">IHA Aarhus School of Engineering</Property>
				<Property Name="INST_autoIncrement" Type="Bool">true</Property>
				<Property Name="INST_buildLocation" Type="Path">/C/Users/au540322/Documents/Projects/BioDiscover/Builds/Installer</Property>
				<Property Name="INST_buildSpecName" Type="Str">SRS Installer</Property>
				<Property Name="INST_defaultDir" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="INST_installerName" Type="Str">install.exe</Property>
				<Property Name="INST_productName" Type="Str">SRS</Property>
				<Property Name="INST_productVersion" Type="Str">1.0.12</Property>
				<Property Name="InstSpecBitness" Type="Str">32-bit</Property>
				<Property Name="InstSpecVersion" Type="Str">20008014</Property>
				<Property Name="MSI_arpCompany" Type="Str">IHA Aarhus School of Engineering</Property>
				<Property Name="MSI_arpContact" Type="Str">mrj@ase.au.dk</Property>
				<Property Name="MSI_arpPhone" Type="Str">+45 20 89 43 32</Property>
				<Property Name="MSI_autoselectDrivers" Type="Bool">true</Property>
				<Property Name="MSI_distID" Type="Str">{D2C484F8-D6B0-4482-9B94-05C3F98D1851}</Property>
				<Property Name="MSI_hideNonRuntimes" Type="Bool">true</Property>
				<Property Name="MSI_osCheck" Type="Int">0</Property>
				<Property Name="MSI_upgradeCode" Type="Str">{85606224-48CC-4369-A748-1FC68DDC1AFB}</Property>
				<Property Name="MSI_windowMessage" Type="Str">Install Species Recognition System (SRS).</Property>
				<Property Name="MSI_windowTitle" Type="Str">SRS Installer</Property>
				<Property Name="RegDest[0].dirName" Type="Str">Software</Property>
				<Property Name="RegDest[0].dirTag" Type="Str">{DDFAFC8B-E728-4AC8-96DE-B920EBB97A86}</Property>
				<Property Name="RegDest[0].parentTag" Type="Str">2</Property>
				<Property Name="RegDestCount" Type="Int">1</Property>
				<Property Name="Source[0].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[0].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[0].name" Type="Str">SRS.exe</Property>
				<Property Name="Source[0].File[0].Shortcut[0].destIndex" Type="Int">0</Property>
				<Property Name="Source[0].File[0].Shortcut[0].name" Type="Str">SRS</Property>
				<Property Name="Source[0].File[0].Shortcut[0].subDir" Type="Str">SRS</Property>
				<Property Name="Source[0].File[0].ShortcutCount" Type="Int">1</Property>
				<Property Name="Source[0].File[0].tag" Type="Str">{A9B9C488-ADD7-40F6-AAC2-547427E5CB24}</Property>
				<Property Name="Source[0].FileCount" Type="Int">1</Property>
				<Property Name="Source[0].name" Type="Str">SRS</Property>
				<Property Name="Source[0].tag" Type="Ref">/My Computer/Build Specifications/SRS</Property>
				<Property Name="Source[0].type" Type="Str">EXE</Property>
				<Property Name="SourceCount" Type="Int">1</Property>
			</Item>
		</Item>
	</Item>
</Project>
