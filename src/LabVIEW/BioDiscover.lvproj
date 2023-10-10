<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="22308000">
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
		<Item Name="assets" Type="Folder">
			<Item Name="Icon.ico" Type="Document" URL="../assets/Icon.ico"/>
		</Item>
		<Item Name="src" Type="Folder">
			<Item Name="Camera" Type="Folder">
				<Item Name="Image Acquisition" Type="Folder">
					<Item Name="Image_Snap_Enqueue.vi" Type="VI" URL="../src/SRS/Image_Snap_Enqueue.vi"/>
					<Item Name="Image_Snap_Dual.vi" Type="VI" URL="../src/SRS/Image_Snap_Dual.vi"/>
					<Item Name="Image_Acquisition_Stop.vi" Type="VI" URL="../src/SRS/Image_Acquisition_Stop.vi"/>
					<Item Name="Image_Snap_Single.vi" Type="VI" URL="../src/SRS/Image_Snap_Single.vi"/>
					<Item Name="Snap2.vi" Type="VI" URL="../src/SRS/Snap2.vi"/>
					<Item Name="Snap4.vi" Type="VI" URL="../src/SRS/Snap4.vi"/>
					<Item Name="Snap16.vi" Type="VI" URL="../src/SRS/Snap16.vi"/>
				</Item>
				<Item Name="Camera_ID.vi" Type="VI" URL="../src/SRS/Camera_ID.vi"/>
				<Item Name="Camera_init.vi" Type="VI" URL="../src/SRS/Camera_init.vi"/>
				<Item Name="Camera_Config.vi" Type="VI" URL="../src/SRS/Camera_Config.vi"/>
				<Item Name="Camera_Config_Specific_Attributes.vi" Type="VI" URL="../src/SRS/Camera_Config_Specific_Attributes.vi"/>
				<Item Name="Camera_Config_Global_Attributes.vi" Type="VI" URL="../src/SRS/Camera_Config_Global_Attributes.vi"/>
				<Item Name="Camera_Capture_Init.vi" Type="VI" URL="../src/SRS/Camera_Capture_Init.vi"/>
				<Item Name="Capture_Save_Initialize.vi" Type="VI" URL="../src/SRS/Capture_Save_Initialize.vi"/>
				<Item Name="Camera_Crop_Setup.vi" Type="VI" URL="../src/SRS/Camera_Crop_Setup.vi"/>
				<Item Name="Camera_Crop_Decluster.vi" Type="VI" URL="../src/SRS/Camera_Crop_Decluster.vi"/>
				<Item Name="CAM_ID_FileLoader.vi" Type="VI" URL="../src/SRS/CAM_ID_FileLoader.vi"/>
				<Item Name="CAM_ID_FileSave.vi" Type="VI" URL="../src/SRS/CAM_ID_FileSave.vi"/>
				<Item Name="CAM_ID_Request.vi" Type="VI" URL="../src/SRS/CAM_ID_Request.vi"/>
				<Item Name="Camera_Crop_X_Axis.vi" Type="VI" URL="../src/SRS/Camera_Crop_X_Axis.vi"/>
				<Item Name="Camera_Crop_Y_Axis.vi" Type="VI" URL="../src/SRS/Camera_Crop_Y_Axis.vi"/>
			</Item>
			<Item Name="Pump and Actuator" Type="Folder">
				<Item Name="Init_XE1000Pump.vi" Type="VI" URL="../src/SRS/Init_XE1000Pump.vi"/>
				<Item Name="Init_L16LinearActuator.vi" Type="VI" URL="../src/SRS/Init_L16LinearActuator.vi"/>
				<Item Name="ID_Connection.vi" Type="VI" URL="../src/SRS/ID_Connection.vi"/>
				<Item Name="Empty_Complete.vi" Type="VI" URL="../src/SRS/Empty_Complete.vi"/>
				<Item Name="System_Serial_Request.vi" Type="VI" URL="../src/SRS/System_Serial_Request.vi"/>
			</Item>
			<Item Name="Images" Type="Folder">
				<Item Name="Save" Type="Folder">
					<Item Name="Image_Folder.vi" Type="VI" URL="../src/SRS/Image_Folder.vi"/>
					<Item Name="Image_Save.vi" Type="VI" URL="../src/SRS/Image_Save.vi"/>
					<Item Name="Folder_Create.vi" Type="VI" URL="../src/SRS/Folder_Create.vi"/>
					<Item Name="Image_Save_Dequeue.vi" Type="VI" URL="../src/SRS/Image_Save_Dequeue.vi"/>
					<Item Name="Image_Save_Handler.vi" Type="VI" URL="../src/SRS/Image_Save_Handler.vi"/>
				</Item>
				<Item Name="Detect and Crop" Type="Folder">
					<Item Name="Image_Handler.vi" Type="VI" URL="../src/SRS/Image_Handler.vi"/>
					<Item Name="Image_Crop_to_Object.vi" Type="VI" URL="../src/SRS/Image_Crop_to_Object.vi"/>
					<Item Name="Image_Detect_Object.vi" Type="VI" URL="../src/SRS/Image_Detect_Object.vi"/>
					<Item Name="Image_Crop_Fixed.vi" Type="VI" URL="../src/SRS/Image_Crop_Fixed.vi"/>
					<Item Name="Image_Crop_Fixed_Area.vi" Type="VI" URL="../src/SRS/Image_Crop_Fixed_Area.vi"/>
					<Item Name="Image_Processing_Queue.vi" Type="VI" URL="../src/SRS/Image_Processing_Queue.vi"/>
					<Item Name="Image_Processing_Queue_Info.vi" Type="VI" URL="../src/SRS/Image_Processing_Queue_Info.vi"/>
					<Item Name="Image_Detect_Object_HQ.vi" Type="VI" URL="../src/SRS/Image_Detect_Object_HQ.vi"/>
					<Item Name="Image_Crop.vi" Type="VI" URL="../src/SRS/Image_Crop.vi"/>
				</Item>
			</Item>
			<Item Name="System" Type="Folder">
				<Item Name="Terminate_Connection.vi" Type="VI" URL="../src/SRS/Terminate_Connection.vi"/>
				<Item Name="Connections.vi" Type="VI" URL="../src/SRS/Connections.vi"/>
				<Item Name="Settings_Load.vi" Type="VI" URL="../src/SRS/Settings_Load.vi"/>
				<Item Name="Settings_Save.vi" Type="VI" URL="../src/SRS/Settings_Save.vi"/>
				<Item Name="Disable Keys.vi" Type="VI" URL="../src/SRS/Disable Keys.vi"/>
				<Item Name="Enable Keys.vi" Type="VI" URL="../src/SRS/Enable Keys.vi"/>
				<Item Name="Get File Info.vi" Type="VI" URL="../src/SRS/Get File Info.vi"/>
				<Item Name="Windows SYSTEMTIME to String.vi" Type="VI" URL="../src/SRS/Windows SYSTEMTIME to String.vi"/>
				<Item Name="Read Exe Version.vi" Type="VI" URL="../src/SRS/Read Exe Version.vi"/>
				<Item Name="Read Exe WriteDate.vi" Type="VI" URL="../src/SRS/Read Exe WriteDate.vi"/>
			</Item>
			<Item Name="Calibration" Type="Folder">
				<Item Name="Calibration_Capture.vi" Type="VI" URL="../src/SRS/Calibration_Capture.vi"/>
				<Item Name="Calibration_Update.vi" Type="VI" URL="../src/SRS/Calibration_Update.vi"/>
				<Item Name="Calibration_Save.vi" Type="VI" URL="../src/SRS/Calibration_Save.vi"/>
				<Item Name="Calibration_Load.vi" Type="VI" URL="../src/SRS/Calibration_Load.vi"/>
				<Item Name="Calibration_Setup_file.vi" Type="VI" URL="../src/SRS/Calibration_Setup_file.vi"/>
			</Item>
			<Item Name="Data Files" Type="Folder">
				<Item Name="CSV_Setup_Data_Create.vi" Type="VI" URL="../src/SRS/CSV_Setup_Data_Create.vi"/>
				<Item Name="CSV_Setup_Data_Handler.vi" Type="VI" URL="../src/SRS/CSV_Setup_Data_Handler.vi"/>
				<Item Name="CSV_Setup_Data_Append.vi" Type="VI" URL="../src/SRS/CSV_Setup_Data_Append.vi"/>
				<Item Name="Sample_Data_Compute.vi" Type="VI" URL="../src/SRS/Sample_Data_Compute.vi"/>
				<Item Name="Sample_Data_Subset.vi" Type="VI" URL="../src/SRS/Sample_Data_Subset.vi"/>
				<Item Name="Save_Folder_Path.vi" Type="VI" URL="../src/SRS/Save_Folder_Path.vi"/>
				<Item Name="CSV_Image_Data_Append.vi" Type="VI" URL="../src/SRS/CSV_Image_Data_Append.vi"/>
				<Item Name="CSV_Image_Data_Create.vi" Type="VI" URL="../src/SRS/CSV_Image_Data_Create.vi"/>
			</Item>
			<Item Name="Controls" Type="Folder">
				<Item Name="Terminate_Pump.ctl" Type="VI" URL="../controls/Terminate_Pump.ctl"/>
				<Item Name="Stop_Program.ctl" Type="VI" URL="../controls/Stop_Program.ctl"/>
			</Item>
			<Item Name="Type Definitions" Type="Folder">
				<Item Name="Data.ctl" Type="VI" URL="../controls/Data.ctl"/>
				<Item Name="State.ctl" Type="VI" URL="../controls/State.ctl"/>
				<Item Name="Camera_ID.ctl" Type="VI" URL="../src/SRS/Camera_ID.ctl"/>
				<Item Name="Image_Data.ctl" Type="VI" URL="../controls/Image_Data.ctl"/>
				<Item Name="CAM_ID.ctl" Type="VI" URL="../src/SRS/CAM_ID.ctl"/>
			</Item>
			<Item Name="misc" Type="Folder">
				<Item Name="Timestamp.vi" Type="VI" URL="../src/SRS/Timestamp.vi"/>
				<Item Name="Timestamp_Converter.vi" Type="VI" URL="../src/SRS/Timestamp_Converter.vi"/>
				<Item Name="Sample_String_Splitter.vi" Type="VI" URL="../src/SRS/Sample_String_Splitter.vi"/>
				<Item Name="Save_Truth_Table.vi" Type="VI" URL="../src/SRS/Save_Truth_Table.vi"/>
				<Item Name="Double2Float.vi" Type="VI" URL="../src/SRS/Double2Float.vi"/>
				<Item Name="Aperture2String.vi" Type="VI" URL="../src/SRS/Aperture2String.vi"/>
				<Item Name="Integer2String.vi" Type="VI" URL="../src/SRS/Integer2String.vi"/>
			</Item>
			<Item Name="MainWindow.vi" Type="VI" URL="../src/SRS/MainWindow.vi"/>
			<Item Name="SRS.rtm" Type="Document" URL="../src/SRS/SRS.rtm"/>
		</Item>
		<Item Name="Test Functions" Type="Folder">
			<Item Name="Camera_Trigger_Manual.vi" Type="VI" URL="../src/SRS/Camera_Trigger_Manual.vi"/>
			<Item Name="Camera_Config_Manual.vi" Type="VI" URL="../src/SRS/Camera_Config_Manual.vi"/>
			<Item Name="CameraStream.vi" Type="VI" URL="../src/SRS/CameraStream.vi"/>
			<Item Name="CameraStreamIMAQ.vi" Type="VI" URL="../src/SRS/CameraStreamIMAQ.vi"/>
			<Item Name="CameraStreamAttribute.vi" Type="VI" URL="../src/SRS/CameraStreamAttribute.vi"/>
			<Item Name="Camera_Reconfig.vi" Type="VI" URL="../src/SRS/Camera_Reconfig.vi"/>
			<Item Name="CameraSerialIDScan.vi" Type="VI" URL="../src/SRS/CameraSerialIDScan.vi"/>
			<Item Name="CameraAttributeSearch.vi" Type="VI" URL="../src/SRS/CameraAttributeSearch.vi"/>
			<Item Name="CameraAttributeTest.vi" Type="VI" URL="../src/SRS/CameraAttributeTest.vi"/>
			<Item Name="USBInterfaceFetch.vi" Type="VI" URL="../src/SRS/USBInterfaceFetch.vi"/>
			<Item Name="Arduino_Communication.vi" Type="VI" URL="../src/SRS/Arduino_Communication.vi"/>
			<Item Name="Enqueue_Acquisition.vi" Type="VI" URL="../src/SRS/Enqueue_Acquisition.vi"/>
			<Item Name="CSV_Setup_Data.vi" Type="VI" URL="../src/SRS/CSV_Setup_Data.vi"/>
			<Item Name="Pump_Status.vi" Type="VI" URL="../src/SRS/Pump_Status.vi"/>
			<Item Name="Bayer12bit.vi" Type="VI" URL="../src/SRS/Bayer12bit.vi"/>
			<Item Name="PumpCommand.vi" Type="VI" URL="../src/SRS/PumpCommand.vi"/>
			<Item Name="httpProducer.vi" Type="VI" URL="../src/SRS/httpProducer.vi"/>
		</Item>
		<Item Name="IHS" Type="Folder">
			<Item Name="Camera" Type="Folder">
				<Item Name="Black_image_detection.vi" Type="VI" URL="../src/IHS/Black_image_detection.vi"/>
				<Item Name="CH VC simplifiseret v2.vi" Type="VI" URL="../src/IHS/CH VC simplifiseret v2.vi"/>
				<Item Name="Convert LabVIEW Image Data To IMAQ.vi" Type="VI" URL="../src/IHS/Convert LabVIEW Image Data To IMAQ.vi"/>
				<Item Name="Errosion_number.vi" Type="VI" URL="../src/IHS/Errosion_number.vi"/>
				<Item Name="Ignore nearby.vi" Type="VI" URL="../src/IHS/Ignore nearby.vi"/>
				<Item Name="Insect_circle_draw.vi" Type="VI" URL="../src/IHS/Insect_circle_draw.vi"/>
				<Item Name="Object_number.vi" Type="VI" URL="../src/IHS/Object_number.vi"/>
				<Item Name="Remove small insects.vi" Type="VI" URL="../src/IHS/Remove small insects.vi"/>
				<Item Name="Sort active pickup area.vi" Type="VI" URL="../src/IHS/Sort active pickup area.vi"/>
				<Item Name="Sort_Insect-data-array_Length.vi" Type="VI" URL="../src/IHS/Sort_Insect-data-array_Length.vi"/>
				<Item Name="Static training image.vi" Type="VI" URL="../src/IHS/Static training image.vi"/>
				<Item Name="UR_task_generator.vi" Type="VI" URL="../src/IHS/UR_task_generator.vi"/>
			</Item>
			<Item Name="Communication" Type="Folder">
				<Item Name="robot_comSUBVI.vi" Type="VI" URL="../src/IHS/robot_comSUBVI.vi"/>
				<Item Name="robot_init.vi" Type="VI" URL="../src/IHS/robot_init.vi"/>
				<Item Name="Robot_listen.vi" Type="VI" URL="../src/IHS/Robot_listen.vi"/>
				<Item Name="Communications test.vi" Type="VI" URL="../src/IHS/Communications test.vi"/>
			</Item>
			<Item Name="Data headlines.vi" Type="VI" URL="../src/IHS/Data headlines.vi"/>
			<Item Name="DBL_2_STRING_ARRAY.vi" Type="VI" URL="../src/IHS/DBL_2_STRING_ARRAY.vi"/>
			<Item Name="Object data correction and extraction.vi" Type="VI" URL="../src/IHS/Object data correction and extraction.vi"/>
			<Item Name="Take and analyse picture.vi" Type="VI" URL="../src/IHS/Take and analyse picture.vi"/>
			<Item Name="Task from tool.vi" Type="VI" URL="../src/IHS/Task from tool.vi"/>
			<Item Name="Tool selector (SubVI).vi" Type="VI" URL="../src/IHS/Tool selector (SubVI).vi"/>
			<Item Name="UR_message_generator.vi" Type="VI" URL="../src/IHS/UR_message_generator.vi"/>
		</Item>
		<Item Name="Main.vi" Type="VI" URL="../src/SRS/Main.vi"/>
		<Item Name="IHS.vi" Type="VI" URL="../src/IHS/IHS.vi"/>
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
				<Item Name="IMAQdx.ctl" Type="VI" URL="/&lt;vilib&gt;/userdefined/High Color/IMAQdx.ctl"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Create"/>
				<Item Name="Imaq Dispose" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/Imaq Dispose"/>
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
				<Item Name="Set Cursor (Icon Pict).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor (Icon Pict).vi"/>
				<Item Name="Set Cursor (Cursor ID).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor (Cursor ID).vi"/>
				<Item Name="Set Cursor.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Cursor.vi"/>
				<Item Name="Set Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Set Busy.vi"/>
				<Item Name="Unset Busy.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/cursorutil.llb/Unset Busy.vi"/>
				<Item Name="Parse State Queue__JKI_lib_State_Machine.vi" Type="VI" URL="/&lt;vilib&gt;/addons/_JKI Toolkits/State Machine/_JKI_lib_State_Machine.llb/Parse State Queue__JKI_lib_State_Machine.vi"/>
				<Item Name="Add State(s) to Queue__JKI_lib_State_Machine.vi" Type="VI" URL="/&lt;vilib&gt;/addons/_JKI Toolkits/State Machine/_JKI_lib_State_Machine.llb/Add State(s) to Queue__JKI_lib_State_Machine.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="FileVersionInfo.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/FileVersionInfo.vi"/>
				<Item Name="FileVersionInformation.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/FileVersionInformation.ctl"/>
				<Item Name="GetFileVersionInfoSize.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/GetFileVersionInfoSize.vi"/>
				<Item Name="BuildErrorSource.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/BuildErrorSource.vi"/>
				<Item Name="GetFileVersionInfo.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/GetFileVersionInfo.vi"/>
				<Item Name="VerQueryValue.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/VerQueryValue.vi"/>
				<Item Name="MoveMemory.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/MoveMemory.vi"/>
				<Item Name="FixedFileInfo_Struct.ctl" Type="VI" URL="/&lt;vilib&gt;/Platform/fileVersionInfo.llb/FixedFileInfo_Struct.ctl"/>
				<Item Name="LV70DateRecToTimeStamp.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/LV70DateRecToTimeStamp.vi"/>
				<Item Name="LV70DateRecToU32.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/LV70DateRecToU32.vi"/>
				<Item Name="Trim Whitespace One-Sided.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace One-Sided.vi"/>
				<Item Name="Get File Extension.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Get File Extension.vi"/>
				<Item Name="Is Path and Not Empty.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Is Path and Not Empty.vi"/>
				<Item Name="Show in File System.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Show in File System.vi"/>
				<Item Name="Read PNG File.vi" Type="VI" URL="/&lt;vilib&gt;/picture/png.llb/Read PNG File.vi"/>
				<Item Name="imagedata.ctl" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/imagedata.ctl"/>
				<Item Name="Check Path.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Check Path.vi"/>
				<Item Name="Directory of Top Level VI.vi" Type="VI" URL="/&lt;vilib&gt;/picture/jpeg.llb/Directory of Top Level VI.vi"/>
				<Item Name="Create Mask By Alpha.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Create Mask By Alpha.vi"/>
				<Item Name="Bit-array To Byte-array.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/Bit-array To Byte-array.vi"/>
				<Item Name="Draw Flattened Pixmap.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Flattened Pixmap.vi"/>
				<Item Name="FixBadRect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/FixBadRect.vi"/>
				<Item Name="Picture to Pixmap.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/Picture to Pixmap.vi"/>
				<Item Name="Simple Grid Descriptor" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Simple Grid Descriptor"/>
				<Item Name="Image Unit" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Unit"/>
				<Item Name="Vision Info Type2.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Vision Info Type2.ctl"/>
				<Item Name="IVA Clear Coordsys Errors.vi" Type="VI" URL="/&lt;vilib&gt;/vision/Vision Assistant Utils.llb/IVA Clear Coordsys Errors.vi"/>
				<Item Name="Imaq GetImageInfo" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/Imaq GetImageInfo"/>
				<Item Name="IVA Store Particles Results.vi" Type="VI" URL="/&lt;vilib&gt;/vision/Vision Assistant Utils.llb/IVA Store Particles Results.vi"/>
				<Item Name="Vision Info Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Vision Info Type"/>
				<Item Name="IVA Result Manager Function.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Vision Assistant Utils.llb/IVA Result Manager Function.ctl"/>
				<Item Name="IVA Append VI Name to GUID.vi" Type="VI" URL="/&lt;vilib&gt;/vision/Vision Assistant Utils.llb/IVA Append VI Name to GUID.vi"/>
				<Item Name="IVA Result Manager.vi" Type="VI" URL="/&lt;vilib&gt;/vision/Vision Assistant Utils.llb/IVA Result Manager.vi"/>
				<Item Name="Sort 2D Array.vim" Type="VI" URL="/&lt;vilib&gt;/Array/Sort 2D Array.vim"/>
				<Item Name="Sort 2D Array - Pop Stack.vi" Type="VI" URL="/&lt;vilib&gt;/Array/Sort 2D Array - Pop Stack.vi"/>
				<Item Name="Sort 2D Array - Push Stack.vi" Type="VI" URL="/&lt;vilib&gt;/Array/Sort 2D Array - Push Stack.vi"/>
				<Item Name="Assert Block Data Type.vim" Type="VI" URL="/&lt;vilib&gt;/Utility/TypeAssert/Assert Block Data Type.vim"/>
				<Item Name="TCP Listen.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen.vi"/>
				<Item Name="Internecine Avoider.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/Internecine Avoider.vi"/>
				<Item Name="TCP Listen List Operations.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen List Operations.ctl"/>
				<Item Name="TCP Listen Internal List.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/tcp.llb/TCP Listen Internal List.vi"/>
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
			<Item Name="imaq.dll" Type="Document" URL="imaq.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="version.dll" Type="Document" URL="version.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="kernel32.dll" Type="Document" URL="kernel32.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="Tag-c(bool,bool).lvlib" Type="Library" URL="/&lt;extravilib&gt;/ChannelInstances/Tag-c(bool,bool).lvlib"/>
			<Item Name="_ChannelSupport.lvlib" Type="Library" URL="/&lt;resource&gt;/ChannelSupport/_ChannelSupport/_ChannelSupport.lvlib"/>
			<Item Name="ChannelProbePositionAndTitle.vi" Type="VI" URL="/&lt;resource&gt;/ChannelSupport/_ChannelSupport/ChannelProbePositionAndTitle.vi"/>
			<Item Name="ChannelProbeWindowStagger.vi" Type="VI" URL="/&lt;resource&gt;/ChannelSupport/_ChannelSupport/ChannelProbeWindowStagger.vi"/>
			<Item Name="Tag-bool.lvlib" Type="Library" URL="/&lt;extravilib&gt;/ChannelInstances/Tag-bool.lvlib"/>
			<Item Name="Tag-t&apos;Data.ctl&apos;.lvlib" Type="Library" URL="/&lt;extravilib&gt;/ChannelInstances/Tag-t&apos;Data.ctl&apos;.lvlib"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="SRS" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{B511CD8F-BE21-4470-A7C4-3ACBADFC72C8}</Property>
				<Property Name="App_INI_GUID" Type="Str">{78EABFCD-5B97-4F87-AF3F-FF129EE73305}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">1</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{2CE40C4E-446A-4350-9E11-C85D8BAE8F13}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">SRS</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/D/Projects/NI_AB_PROJECTNAME/Builds/bin/Full Build</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{09FD23A0-93D2-46A2-B12D-FA02255F97C6}</Property>
				<Property Name="Bld_version.build" Type="Int">36</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Bld_version.minor" Type="Int">9</Property>
				<Property Name="Bld_version.patch" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">SRS.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/D/Projects/NI_AB_PROJECTNAME/Builds/bin/Full Build/SRS.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">/D/Projects/NI_AB_PROJECTNAME/Builds/bin/Full Build/data</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{D4542A37-FE92-4089-827A-E0D373127B59}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Main.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Show toolbar</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">1</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/src/Controls</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/src/Type Definitions</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/src/SRS.rtm</Property>
				<Property Name="Source[4].lvfile" Type="Bool">true</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/assets</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="SourceCount" Type="Int">6</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Species Recognition System - beta</Property>
				<Property Name="TgtF_internalName" Type="Str">SRS</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2012 </Property>
				<Property Name="TgtF_productName" Type="Str">SRS</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{A9B9C488-ADD7-40F6-AAC2-547427E5CB24}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">SRS.exe</Property>
			</Item>
			<Item Name="IHS" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{AC24E754-434A-4853-85D8-9CC4F46CA368}</Property>
				<Property Name="App_INI_GUID" Type="Str">{2F6E04B7-A84D-42D2-8A54-F5F8E4CD910F}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">1</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{34038B49-5878-4C77-9BCB-331853165D8C}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">IHS</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/D/Projects/NI_AB_PROJECTNAME/Builds/bin/IHS</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{9AC70069-B77D-48A2-858D-76D34FC679AD}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">IHS.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/D/Projects/NI_AB_PROJECTNAME/Builds/bin/IHS/IHS.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">/D/Projects/NI_AB_PROJECTNAME/Builds/bin/IHS/data</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{D4542A37-FE92-4089-827A-E0D373127B59}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Main.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Show toolbar</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">1</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/src/Controls</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/src/Type Definitions</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/src/SRS.rtm</Property>
				<Property Name="Source[4].lvfile" Type="Bool">true</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/assets</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/My Computer/IHS.vi</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[6].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">7</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Species Recognition System - beta</Property>
				<Property Name="TgtF_internalName" Type="Str">SRS</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2012 </Property>
				<Property Name="TgtF_productName" Type="Str">SRS</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{8A6E9157-7132-417F-BF00-B9EE27F0A6EF}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">IHS.exe</Property>
			</Item>
			<Item Name="Installer" Type="Installer">
				<Property Name="Destination[0].name" Type="Str">SRS</Property>
				<Property Name="Destination[0].parent" Type="Str">{3912416A-D2E5-411B-AFEE-B63654D690C0}</Property>
				<Property Name="Destination[0].tag" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Destination[0].type" Type="Str">userFolder</Property>
				<Property Name="Destination[0].unlock" Type="Bool">true</Property>
				<Property Name="DestinationCount" Type="Int">1</Property>
				<Property Name="DistPart[0].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[0].productID" Type="Str">{C8E6A834-3F86-4C97-A020-8DE0F5522BF9}</Property>
				<Property Name="DistPart[0].productName" Type="Str">NI Vision Common Resources 2023 Q1</Property>
				<Property Name="DistPart[0].upgradeCode" Type="Str">{409BEFA9-EB3E-472F-AD77-271A4A1D5927}</Property>
				<Property Name="DistPart[1].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[1].productID" Type="Str">{31AB186F-BCAD-4EF6-9192-7D44C7587B99}</Property>
				<Property Name="DistPart[1].productName" Type="Str">NI Vision Runtime 2023 Q1</Property>
				<Property Name="DistPart[1].upgradeCode" Type="Str">{63DF74E5-A5C9-11D4-814E-005004D6CDD6}</Property>
				<Property Name="DistPart[2].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[2].productID" Type="Str">{45E21CB8-05D7-4E12-B56D-2DDF6EC5B1CB}</Property>
				<Property Name="DistPart[2].productName" Type="Str">NI-488.2 Runtime 23.5</Property>
				<Property Name="DistPart[2].upgradeCode" Type="Str">{357F6618-C660-41A2-A185-5578CC876D1D}</Property>
				<Property Name="DistPart[3].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[3].productID" Type="Str">{600831DA-D9CA-4B20-A4B3-3293A741324F}</Property>
				<Property Name="DistPart[3].productName" Type="Str">NI-IMAQdx Runtime 23.0</Property>
				<Property Name="DistPart[3].upgradeCode" Type="Str">{3D104AB3-CE10-43C0-B647-07600754072C}</Property>
				<Property Name="DistPart[4].flavorID" Type="Str">_full_</Property>
				<Property Name="DistPart[4].productID" Type="Str">{ECF7D15D-85F8-4DE3-B7AC-294D306FA70F}</Property>
				<Property Name="DistPart[4].productName" Type="Str">NI-Serial Runtime 23.3</Property>
				<Property Name="DistPart[4].upgradeCode" Type="Str">{01D82F43-B48D-46FF-8601-FC4FAAE20F41}</Property>
				<Property Name="DistPart[5].flavorID" Type="Str">_deployment_</Property>
				<Property Name="DistPart[5].productID" Type="Str">{95D24B70-E5A0-4A12-B606-D732ADB7DC8F}</Property>
				<Property Name="DistPart[5].productName" Type="Str">NI-VISA Runtime 23.5</Property>
				<Property Name="DistPart[5].upgradeCode" Type="Str">{8627993A-3F66-483C-A562-0D3BA3F267B1}</Property>
				<Property Name="DistPart[6].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[6].productID" Type="Str">{3954BD22-4321-42BB-BA6C-F687895AD8F0}</Property>
				<Property Name="DistPart[6].productName" Type="Str">NI LabVIEW Runtime 2022 Q3 Patch 1 (64-bit)</Property>
				<Property Name="DistPart[6].SoftDep[0].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[0].productName" Type="Str">NI ActiveX Container (64-bit)</Property>
				<Property Name="DistPart[6].SoftDep[0].upgradeCode" Type="Str">{1038A887-23E1-4289-B0BD-0C4B83C6BA21}</Property>
				<Property Name="DistPart[6].SoftDep[1].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[1].productName" Type="Str">NI Deployment Framework 2022 (64-bit)</Property>
				<Property Name="DistPart[6].SoftDep[1].upgradeCode" Type="Str">{E0D3C7F9-4512-438F-8123-E2050457972B}</Property>
				<Property Name="DistPart[6].SoftDep[10].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[10].productName" Type="Str">NI TDM Streaming 22.3</Property>
				<Property Name="DistPart[6].SoftDep[10].upgradeCode" Type="Str">{4CD11BE6-6BB7-4082-8A27-C13771BC309B}</Property>
				<Property Name="DistPart[6].SoftDep[2].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[2].productName" Type="Str">NI Error Reporting 2020 (64-bit)</Property>
				<Property Name="DistPart[6].SoftDep[2].upgradeCode" Type="Str">{785BE224-E5B2-46A5-ADCB-55C949B5C9C7}</Property>
				<Property Name="DistPart[6].SoftDep[3].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[3].productName" Type="Str">NI LabVIEW Real-Time NBFifo 2022</Property>
				<Property Name="DistPart[6].SoftDep[3].upgradeCode" Type="Str">{68688466-B146-325C-AC08-D6ADFE5A4205}</Property>
				<Property Name="DistPart[6].SoftDep[4].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[4].productName" Type="Str">NI Logos 22.3</Property>
				<Property Name="DistPart[6].SoftDep[4].upgradeCode" Type="Str">{5E4A4CE3-4D06-11D4-8B22-006008C16337}</Property>
				<Property Name="DistPart[6].SoftDep[5].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[5].productName" Type="Str">NI LabVIEW Web Server 2022 (64-bit)</Property>
				<Property Name="DistPart[6].SoftDep[5].upgradeCode" Type="Str">{5F449D4C-83B9-492E-986B-6B85A29C431D}</Property>
				<Property Name="DistPart[6].SoftDep[6].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[6].productName" Type="Str">NI mDNS Responder 22.5</Property>
				<Property Name="DistPart[6].SoftDep[6].upgradeCode" Type="Str">{9607874B-4BB3-42CB-B450-A2F5EF60BA3B}</Property>
				<Property Name="DistPart[6].SoftDep[7].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[7].productName" Type="Str">Math Kernel Libraries 2017</Property>
				<Property Name="DistPart[6].SoftDep[7].upgradeCode" Type="Str">{699C1AC5-2CF2-4745-9674-B19536EBA8A3}</Property>
				<Property Name="DistPart[6].SoftDep[8].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[8].productName" Type="Str">Math Kernel Libraries 2020</Property>
				<Property Name="DistPart[6].SoftDep[8].upgradeCode" Type="Str">{9872BBBA-FB96-42A4-80A2-9605AC5CBCF1}</Property>
				<Property Name="DistPart[6].SoftDep[9].exclude" Type="Bool">false</Property>
				<Property Name="DistPart[6].SoftDep[9].productName" Type="Str">NI VC2015 Runtime</Property>
				<Property Name="DistPart[6].SoftDep[9].upgradeCode" Type="Str">{D42E7BAE-6589-4570-B6A3-3E28889392E7}</Property>
				<Property Name="DistPart[6].SoftDepCount" Type="Int">11</Property>
				<Property Name="DistPart[6].upgradeCode" Type="Str">{FB80C6B7-18E1-3FF4-99A2-719F62FACAD8}</Property>
				<Property Name="DistPartCount" Type="Int">7</Property>
				<Property Name="INST_author" Type="Str">IHA Aarhus School of Engineering</Property>
				<Property Name="INST_autoIncrement" Type="Bool">true</Property>
				<Property Name="INST_buildLocation" Type="Path">/D/Projects/BioDiscover/Builds/bin/Installer</Property>
				<Property Name="INST_buildSpecName" Type="Str">Installer</Property>
				<Property Name="INST_defaultDir" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="INST_installerName" Type="Str">install.exe</Property>
				<Property Name="INST_productName" Type="Str">SRS</Property>
				<Property Name="INST_productVersion" Type="Str">1.0.38</Property>
				<Property Name="InstSpecBitness" Type="Str">64-bit</Property>
				<Property Name="InstSpecVersion" Type="Str">22308000</Property>
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
				<Property Name="Source[0].File[0].tag" Type="Str">{A9B9C488-ADD7-40F6-AAC2-547427E5CB24}</Property>
				<Property Name="Source[0].File[1].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[1].name" Type="Str">SRS.aliases</Property>
				<Property Name="Source[0].File[1].tag" Type="Str">{B511CD8F-BE21-4470-A7C4-3ACBADFC72C8}</Property>
				<Property Name="Source[0].File[2].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[2].name" Type="Str">SRS.ini</Property>
				<Property Name="Source[0].File[2].tag" Type="Str">{78EABFCD-5B97-4F87-AF3F-FF129EE73305}</Property>
				<Property Name="Source[0].FileCount" Type="Int">1</Property>
				<Property Name="Source[0].name" Type="Str">SRS</Property>
				<Property Name="Source[0].tag" Type="Ref">/My Computer/Build Specifications/SRS</Property>
				<Property Name="Source[0].type" Type="Str">EXE</Property>
				<Property Name="Source[1].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[1].File[0].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[1].File[0].name" Type="Str">IHS.exe</Property>
				<Property Name="Source[1].File[0].tag" Type="Str">{8A6E9157-7132-417F-BF00-B9EE27F0A6EF}</Property>
				<Property Name="Source[1].FileCount" Type="Int">1</Property>
				<Property Name="Source[1].name" Type="Str">IHS</Property>
				<Property Name="Source[1].tag" Type="Ref">/My Computer/Build Specifications/IHS</Property>
				<Property Name="Source[1].type" Type="Str">EXE</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
			</Item>
			<Item Name="Update" Type="Installer">
				<Property Name="Destination[0].name" Type="Str">SRS</Property>
				<Property Name="Destination[0].parent" Type="Str">{3912416A-D2E5-411B-AFEE-B63654D690C0}</Property>
				<Property Name="Destination[0].tag" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Destination[0].type" Type="Str">userFolder</Property>
				<Property Name="Destination[0].unlock" Type="Bool">true</Property>
				<Property Name="DestinationCount" Type="Int">1</Property>
				<Property Name="INST_author" Type="Str">IHA Aarhus School of Engineering</Property>
				<Property Name="INST_autoIncrement" Type="Bool">true</Property>
				<Property Name="INST_buildLocation" Type="Path">/D/Projects/BioDiscover/Builds/bin/Update</Property>
				<Property Name="INST_buildSpecName" Type="Str">Update</Property>
				<Property Name="INST_defaultDir" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="INST_installerName" Type="Str">update.exe</Property>
				<Property Name="INST_productName" Type="Str">SRS</Property>
				<Property Name="INST_productVersion" Type="Str">1.0.47</Property>
				<Property Name="InstSpecBitness" Type="Str">64-bit</Property>
				<Property Name="InstSpecVersion" Type="Str">22308000</Property>
				<Property Name="MSI_arpCompany" Type="Str">IHA Aarhus School of Engineering</Property>
				<Property Name="MSI_arpContact" Type="Str">mrj@ase.au.dk</Property>
				<Property Name="MSI_arpPhone" Type="Str">+45 20 89 43 32</Property>
				<Property Name="MSI_distID" Type="Str">{DB3884D9-03B3-4BEC-94CA-9165C9AE9E32}</Property>
				<Property Name="MSI_osCheck" Type="Int">0</Property>
				<Property Name="MSI_upgradeCode" Type="Str">{A81C79D8-3CE4-4E42-A8D8-5F59C163A19B}</Property>
				<Property Name="MSI_windowMessage" Type="Str">Install Species Recognition System (SRS).</Property>
				<Property Name="MSI_windowTitle" Type="Str">SRS Installer</Property>
				<Property Name="RegDest[0].dirName" Type="Str">Software</Property>
				<Property Name="RegDest[0].dirTag" Type="Str">{DDFAFC8B-E728-4AC8-96DE-B920EBB97A86}</Property>
				<Property Name="RegDest[0].parentTag" Type="Str">2</Property>
				<Property Name="RegDestCount" Type="Int">1</Property>
				<Property Name="Source[0].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[0].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[0].name" Type="Str">SRS.exe</Property>
				<Property Name="Source[0].File[0].tag" Type="Str">{A9B9C488-ADD7-40F6-AAC2-547427E5CB24}</Property>
				<Property Name="Source[0].File[1].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[1].name" Type="Str">SRS.aliases</Property>
				<Property Name="Source[0].File[1].tag" Type="Str">{B511CD8F-BE21-4470-A7C4-3ACBADFC72C8}</Property>
				<Property Name="Source[0].File[2].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[0].File[2].name" Type="Str">SRS.ini</Property>
				<Property Name="Source[0].File[2].tag" Type="Str">{78EABFCD-5B97-4F87-AF3F-FF129EE73305}</Property>
				<Property Name="Source[0].name" Type="Str">SRS</Property>
				<Property Name="Source[0].tag" Type="Ref">/My Computer/Build Specifications/SRS</Property>
				<Property Name="Source[0].type" Type="Str">EXE</Property>
				<Property Name="Source[1].dest" Type="Str">{81EECF78-BC3B-46C6-808D-DC0484F07179}</Property>
				<Property Name="Source[1].name" Type="Str">IHS</Property>
				<Property Name="Source[1].tag" Type="Ref">/My Computer/Build Specifications/IHS</Property>
				<Property Name="Source[1].type" Type="Str">EXE</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
			</Item>
		</Item>
	</Item>
</Project>
