Ports: 
	COM 7 - Label 034G2330 - Installed at buttom of the block - Brown cable extension -  Green & Brown 
	COM 10 - Label 034G2330(Scrateched with orange & blue marking) - Installed at top of block - Black cable extension - Reads higher RH v 	alues - Blue & orange

Map:
	RH : Mapped from 0 to 100% --> 0 to 255 on PWM --> Voltage read 0 to 5V
	Tempreture : Mapped from -40 to 60 --> 0 to 255 on PWM --> Voltage read 0 to 5V (bellow range goes to 0 and above to 5V)

Data structure:
	Serial.println("RH[%],RH_255, PPartial[Pa]*10, Var_PPartial,  Temp[degC], Temp_255");
 