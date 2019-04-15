
Common =		{
				"NEEDSENCODING": "needsEncoding",
				"ENCODED": "encoded",
				"DECODED": "decoded",
				"MYENCODER": "myEncoder",
			}

Containers = 		{
				"ENVELOPE": "ENVELOPE",
				"RPDU": "RPDU",
				"SMS": "SMS",
				"UD": "UD",
				"WSP": "WSP",
				"WBXML": "WBXML",
				"SIMCMD": "SIM_CMD",
				"MMS": "MMS",
			}

ENVELOPE =		{
				"CLA" : "CLA",
				"INS" : "INS",
				"P1": "P1",	
				"P2": "P2",
				"LEN": "LEN",
				"BERTLV": "BERTLV",
				"BERTLVTAG": "BERTLVTag",
				"BERTLVLEN": "BERTLVLen",
				"SIMPLETLV": "SimpleTLV",
				"SIMPLETLVTAG": "SimpleTLVTag",
				"SIMPLETLVLEN": "SimpleTLVLen",
				"SIMPLETLVVAL": "SimpleTLVVal",
				"LASTSIMPLETLVLENFLAG": "LastSimpleTLVLenFlag",
	     		}

ENVELOPE_parse =	{
				"CLA" : "CLA",
				"INS" : "INS",
				"P1": "P1",	
				"P2": "P2",
				"GenLEN": "GenerateLEN",
				"LEN": "LEN",
				"BERTLVTag": "BERTLVTag",
				"GenBERTLVLen": "GenerateBERTLVLen",
				"BERTLVLen": "BERTLVLen",
				"SimpleTLVTag": "SimpleTLVTag",
				"GenSimpleTLVLen": "GenerateSimpleTLVLen",
				"SimpleTLVLen": "SimpleTLVLen",
				"SimpleTLVVal": "SimpleTLVVal",
				"LastSimpleTLVLenFlag": "LastSimpleTLVLenFlag",
	     		}

RPDU =		 	{
				"RPOA" : "RPOA",
				"RPDA" : "RPDA",
				"RPDUMTI": "RPDU-MTI",	
				"RPDUMR": "RPDU-MR",
				"RPOALEN": "RPOALength",
				"RPOANO": "RPOANumber",
				"RPDALEN": "RPDALength",
				"RPDANO": "RPDANumber",
				"RPUDL": "RPUDL",
				"RPUDTYPE": "RPUDType",
				"RPCAUSELEN": "RPCauseLength",
				"RPCAUSE": "RPCause",
	     		}

RPDU_parse =	 	{
				"MTI": "MTI",	
				"MR": "MR",
				"GenRPOALen": "GenerateRPOALength",	
				"RPOALen": "RPOALength",
				"GenEncRPOA": "GenerateEncodedRPOA",
				"EncRPOA": "EncodedRPOA",
				"DecRPOA": "DecodedRPOA",
				"GenRPDALen": "GenerateRPDALength",
				"RPDALen": "RPDALength",
				"GenEncRPDA": "GenerateEncodedRPDA",
				"EncRPDA": "EncodedRPDA",
				"DecRPDA": "DecodedRPDA",
				"GenRPUDL": "GenerateRPUDL",
				"RPUDL": "RPUDL",
				"RPUDType": "RPUDType",
				"GenRPCauseLen": "GenerateRPCauseLength",
				"RPCauseLen": "RPCauseLength",
				"RPCause": "RPCause",
	     		}

SMS =			{	
				"SMSTYPE": "explicitSMSType",
				"EXCLSMSCHDR": "excludeSMSCHeader",
				"SMSC": "SMSC",
				"SMSCLEN": "SMSCLength",
				"SMSCTYPE": "SMSCType",
				"SMSCNUM": "SMSCNumber",
				"SEND": "Sender",
				"SENDLEN": "SenderLength",
				"SENDTYPE": "SenderType",
				"SENDNUM": "SenderNumber",		
				"MR": "MR",
				"SCTS": "SCTS",
				"VP": "VP",
				"PDUTYPE": "PDUType",
				"PID": "PID",
				"PI": "PI",
				"FCS": "FCS",
				"DCS": "DCS",
			}

SMS_parse =		{	
				"ExclSMSCHdr": "ExcludeSMSCHeader",
				"GenSMSCLen": "GenerateSMSCLength",
				"SMSCLen": "SMSCLength",
				"SMSCType": "SMSCType",
				"GenEncSMSCNum": "GenerateEncodedSMSCNum",
				"EncSMSCNum": "EncodedSMSCNum",
				"DecSMSCNum": "DecodedSMSCNum",
				"GenSendLen": "GenerateSenderLength",
				"SendLen": "SenderLength",
				"SendType": "SenderType",
				"GenEncSendNum": "GenerateEncodedSenderNum",
				"EncSendNum": "EncodedSenderNum",
				"DecSendNum": "DecodedSenderNum",		
				"MR": "MR",
				"SCTS": "SCTS",
				"RPDUfile": "RPDUfile",
				"UDFile": "UDFile",
				"WSPFile": "WSPFile",
				"WBXMLFile": "WBXMLFile",
				"SIMCMDFile": "SIMCMDFile",
				"MMSFile": "MMSFile",
				"EnvelopeFile": "EnvelopeFile",
				"VP": "VP",
				"PDUType": "PDUType",
				"PID": "PID",
				"DCS": "DCS",
				"PI": "PI",
				"FCS": "FCS",
				"SMSType": "SMSType",
			}

UD =		 	{	
				"UDL": "UDL",
				"USRDATA": "UserData",
				"UDHL": "UDHL",
				"IE": "IE",
				"IELEN": "IELength",
				"IETYPE": "IEType",
				"IEDATA": "IEData",
	     		}

UD_parse =	 	{
				"GenUDL": "GenerateUDL",	
				"UDL": "UDL",
				"GenEncUD": "GenerateEncodedUD",	
				"EncUD": "EncodedUD",
				"DecUD": "DecodedUD",
				"GenUDHL": "GenerateUDHL",
				"UDHL": "UDHL",
				"GenIELen": "GenerateIELength",
				"IELen": "IELength",
				"IEType": "IEType",
				"GenEncIED": "GenerateEncodedIED",
				"EncIED": "EncodedIED",
				"DecIED": "DecodedIED",
	     		}


WSP =			{	
				"WSPTID": "WSP-TID",
				"WSPTYPE": "WSPType",
				"WSPHL": "WSP-HL",
				"WSPCONTTYPE": "WSPContentType",
				"WSPHDRS": "WSPHeaders",
			}

WSP_parse =	 	{
				"WSPTID": "WSPTID",
				"WSPType": "WSPType",
				"GenWSPHL": "GenerateWSPHL",
				"WSPHL": "WSPHL",
				"GenEncContType": "GenerateEncodedContentType",
				"EncContType": "EncodedContentType",
				"DecContType": "DecodedContentType",
				"GenEncHdrs": "GenerateEncodedHeaders",
				"EncHdrs": "EncodedHeaders",
				"DecHdrs": "DecodedHeaders",		
	     		}

WBXML =	 		{
				"WBXML": "WBXML",	
				"WBXMLVERS": "WBXMLVersion",
	     		}

WBXML_parse =	 	{
				"GenEncWBXML": "GenerateEncodedWBXML",		
				"EncWBXML": "EncodedWBXML",
				"DecWBXML": "DecodedWBXML",
				"WBXMLVers": "WBXMLVersion",
	     		}

SIMCMD =		{	
				"CPL": "CPL",	
				"CHL": "CHL",
				"SPI": "SPI",
				"KiC": "KiC",
				"KiD": "KiD",
				"TAR": "TAR",
				"CNTR": "CNTR",
				"PCNTR": "PCNTR",
				"RC_CC_DS": "RC/CC/DS",
				"SECDATA": "SECURED_DATA",
			}

SIMCMD_parse =	 	{
				"GenCPL": "GenerateCPL",
				"CPL": "CPL",
				"GenCHL": "GenerateCHL",
				"SPI": "SPI",	
				"CHL": "CHL",
				"KiC": "KiC",
				"KiD": "KiD",
				"TAR": "TAR",
				"CNTR": "CNTR",
				"PCNTR": "PCNTR",
				"RC_CC_DS": "RC_CC_DS",
				"GenSecData": "GenerateSecData",
				"EncSecData": "EncodedSecData",	
				"DecSecData": "DecodedSecData",
	     		}

MMS =    	 	{
				"MSGTYPE": "MsgType",
				"TID": "TID",
				"VERS": "Version",
				"FROM": "From",
				"SUBJ": "Subject",
				"MSGCLS": "MsgClass",
				"MSGSIZE": "MsgSize",
				"EXP": "Expiry",
				"CNTLOC": "ContentLoc",
	     		}

MMS_parse =	 	{
				"MsgType": "MsgType",
				"TID": "TID",
				"Vers": "Version",
				"From": "From",
				"Subj": "Subject",
				"MsgCls": "MsgClass",
				"MsgSize": "MsgSize",
				"Exp": "Expiry",
				"CntLoc": "ContentLoc",
	     		}

			
