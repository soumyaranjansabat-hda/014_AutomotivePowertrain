
1. DBC: opendbc https://github.com/commaai/opendbc/tree/master

2. Problems/Changes done -

    tesla_can.dbc : Doesnt open in directly in Vector CANdb++ Editor. I have now manually updated the following: 
                    Removed the items -
                    VAL_ 568 UI_mapSpeedLimit 31 "SNA" 30 "UNLIMITED" 29 "LESS_OR_EQ_160" 28 "LESS_OR_EQ_150" 27 "LESS_OR_EQ_140" 26 "LESS_OR_EQ_130" 25 "LESS_OR_EQ_120" 24 "LESS_OR_EQ_115" 23 "LESS_OR_EQ_110" 22 "LESS_OR_EQ_105" 21 "LESS_OR_EQ_100" 20 "LESS_OR_EQ_95" 19 "LESS_OR_EQ_90" 18 "LESS_OR_EQ_85" 17 "LESS_OR_EQ_80" 16 "LESS_OR_EQ_75" 15 "LESS_OR_EQ_70" 14 "LESS_OR_EQ_65" 13 "LESS_OR_EQ_60" 12 "LESS_OR_EQ_55" 11 "LESS_OR_EQ_50" 10 "LESS_OR_EQ_45" 9 "LESS_OR_EQ_40" 8 "LESS_OR_EQ_35" 7 "LESS_OR_EQ_30" 6 "LESS_OR_EQ_25" 5 "LESS_OR_EQ_20" 4 "LESS_OR_EQ_15" 3 "LESS_OR_EQ_10" 2 "LESS_OR_EQ_7" 1 "LESS_OR_EQ_5" 0 "UNKNOWN" ;
                    783
                    
    tesla_model3_vehicle.dbc : Doesnt open in directly in Vector CANdb++ Editor. I have manually added the NS_ and BS_

4. The Tesla related "generated" files are generated through python functions
