
from webcrawler.lenses import datakeys

#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_DICTs
#/////////////////////////

TESTDATA_DICT_WITHOUT_VALUES = {
    datakeys.key_name_as_pl: "",
    datakeys.key_focal_length_as_pl: "",
    datakeys.key_aperture_as_pl: "",
    datakeys.key_filter_as_pl: "",
    datakeys.key_magnification_as_pl: "",
    datakeys.key_minimalfocus_as_pl: "",
    datakeys.key_mount_as_pl: "",
    datakeys.key_sensor_compatibility_as_pl: "",
    datakeys.key_weight_as_pl: "",
    datakeys.key_size_as_pl: ""
}

TESTDATA_DICT_FULL1 = {
    datakeys.key_name_as_pl: "Nikon AF-P DX NIKKOR 10-20mm f/4.5-5.6G VR ",
    datakeys.key_focal_length_as_pl: "10-20mm",
    datakeys.key_aperture_as_pl: "f/4.5",
    datakeys.key_filter_as_pl: "72mm",
    datakeys.key_magnification_as_pl: "0.17x",
    datakeys.key_minimalfocus_as_pl: "0.8 ft. (0.22 m)",
    datakeys.key_mount_as_pl: "Nikon F",
    datakeys.key_sensor_compatibility_as_pl: "APS-C / DX",
    datakeys.key_weight_as_pl: "8.2 oz. (230 g)",
    datakeys.key_size_as_pl: "3.0 in. (77 mm) x 2.8 in. (73mm)"
}




#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_RAW_HTML_STRINGs
#/////////////////////////

TESTDATA_RAW_HTML_TABLE_STRING_FULL1 = ' \
"<table width="100%" id="rounded-corner" summary="Nikon AF-P DX NIKKOR 10-20mm f/4.5-5.6G VR"> \
<thead><tr><th scope="col" class="rounded-header" width="60%">Lens Specifications</th><th scope=" \
col" align="center"  width="40%" class="rounded-right"></th></tr></thead><tfoot><tr><td colspan="2" \
 class="rounded-foot-left-right"></td></tr></tfoot><tbody><tr><td>Lens Type</td><td>Zoom Lens</td> \
</tr><tr><td>Focal Length</td><td>10-20mm</td></tr><tr><td>Mount Type</td><td>Nikon F</tr><tr><td> \
Format</td><td>APS-C / DX</td></tr><tr><td>Compatible Format(s)</td><td>APS-C</td></tr><tr><td> \
Compatible with Teleconverters</td><td>No</td></tr><tr><td>Zoom Ratio</td><td>2x</td></tr><tr><td> \
Maximum Reproduction Ratio</td><td>0.17x</td></tr><tr><td>Vibration Reduction (Image Stabilization) \
</td><td>No</td></tr><tr><th scope="col" colspan="2">Aperture Information</th></tr><tr><td>Aperture Ring \
</td><td>No</td></tr><tr><td>Maximum Aperture</td><td>f/4.5</td></tr><tr><td>Minimum Aperture</td> \
<td>f/29</td></tr><tr><td>Maximum Angle of View (APS-C or smaller format)</td><td>109°</td></tr><tr> \
<td>Minimum Angle of View (APS-C or smaller format)</td><td>70°</td></tr><tr><th scope="col" colspan="2"> \
Optical Information</th></tr><tr><td>Lens Elements</td><td>14</td></tr><tr><td>Lens Groups</td><td>11 \
</td></tr><tr><td>Diaphragm Blades</td><td>7 (Rounded)</td></tr><tr><td>Aspherical Elements</td><td>3 \
</td></tr><tr><td>Nano Crystal Coat</td><td>No</td></tr><tr><td>Super Integrated Coat (SIC)</td><td>Yes \
</td></tr><tr><th scope="col" colspan="2">Focus Information</th></tr><tr><td>Focus</td><td>Autofocus</td> \
</tr><tr><td>Built-in Focus Motor</td><td>Yes</td></tr><tr><td>Silent Wave Motor (SWM)</td><td>No</td> \
</tr><tr><td>Pulse Motor (AF-P)</td><td>Yes</td></tr><tr><td>Internal Focusing</td><td>Yes</td></tr><tr> \
<td>Minimum Focus Distance</td><td>0.8 ft. (0.22 m)</td></tr><tr><td>Focus Mode Switch</td><td>Auto / Manual \
</td></tr><tr><td>G-type</td><td>Yes</td></tr><tr><th scope="col" colspan="2">Filter Information</th></tr> \
<tr><td>Filter Size</td><td>72mm</td></tr><tr><td>Accepts Filter Type</td><td>Screw-on</td></tr><tr> \
<th scope="col" colspan="2">Physical Characteristics</th></tr><tr><td>Weather / Dust Sealing</td><td>No</td> \
</tr><tr><td>Mount Material</td><td>Plastic</td></tr><tr><td>Tripod Collar</td><td>No</td></tr><tr> \
<td>Dimensions</td><td>3.0 in. (77 mm) x 2.8 in. (73 mm)</td></tr><tr><td>Weight</td><td>8.2 oz. (230 g) \
</td></tr><tr><th scope="col" colspan="2">Other Information</th></tr><tr><td>Available in Colors</td> \
<td>Black</td></tr></tbody></table>"'

TESTDATA_DICT_FULL2 = ' \
<table width="100%" id="rounded-corner" summary="Pentax HD PENTAX-DA 21mm f/3.2 AL Limited"> \
<thead><tr><th scope="col" class="rounded-header" width="60%">Lens Specifications</th> \
<th scope="col" align="center"  width="40%" class="rounded-right"></th></tr></thead><tfoot><tr> \
<td colspan="2" class="rounded-foot-left-right"></td></tr></tfoot><tbody><tr><td>Lens Type</td> \
<td>Prime Lens</td></tr><tr><td>Focal Length</td><td>21mm</td></tr><tr><td>Mount Type</td> \
<td>Pentax K</tr><tr><td>Format</td><td>APS-C / DX</td></tr><tr><td>Compatible Format(s)</td><td>APS-C</td> \
</tr><tr><td>Compatible with Teleconverters</td><td>No</td></tr><tr><td>Maximum Reproduction Ratio</td><td>0.17x</td> \
</tr><tr><td>Shake Reduction (Image Stabilization)</td><td>No</td></tr><tr> \
<th scope="col" colspan="2">Aperture Information</th></tr><tr><td>Aperture Ring</td><td>No</td> \
</tr><tr><td>Maximum Aperture</td><td>f/3.2</td></tr><tr><td>Minimum Aperture</td><td>f/22</td> \
</tr><tr><td>Maximum Angle of View (APS-C or smaller format)</td><td>68°</td></tr><tr> \
<th scope="col" colspan="2">Optical Information</th></tr><tr><td>Lens Elements</td><td>8</td> \
</tr><tr><td>Lens Groups</td><td>5</td></tr><tr><td>Diaphragm Blades</td><td>7</td></tr><tr> \
<td>HD Coating</td><td>No</td></tr><tr><td>Super-Multi Coating (SMC)</td><td>No</td></tr><tr> \
<th scope="col" colspan="2">Focus Information</th></tr><tr><td>Focus</td><td>Autofocus</td></tr> \
<tr><td>Built-in Focus Motor</td><td>Yes</td></tr><tr><td>Supersonic Direct-drive Motor (SDM)</td> \
<td>No</td></tr><tr><td>Minimum Focus Distance</td><td>0.20m</td></tr><tr><td>Distance Information</td> \
<td>Yes</td></tr><tr><th scope="col" colspan="2">Filter Information</th></tr><tr><td>Filter Size</td> \
<td>49mm</td></tr><tr><td>Accepts Filter Type</td><td>Screw-on</td></tr><tr> \
<th scope="col" colspan="2">Physical Characteristics</th></tr><tr><td>Weather / Dust Sealing</td><td>No</td> \
</tr><tr><td>Mount Material</td><td>Metal</td></tr><tr><td>Tripod Collar</td><td>No</td></tr><tr><td>Dimensions</td> \
<td>63.50 x 25.40mm</td></tr><tr><td>Weight</td><td>119g</td></tr><tr><th scope="col" colspan="2">Other Information</th> \
</tr><tr><td>Available in Colors</td><td>Black</td></tr></tbody></table>'

TESTDATA_DICT_FULL3 = ' \
<table width="100%" id="rounded-corner" summary="Fujifilm XF 50mm f/2 R WR"><thead><tr> \
<th scope="col" class="rounded-header" width="60%">Lens Specifications</th> \
<th scope="col" align="center"  width="40%" class="rounded-right"></th></tr></thead><tfoot><tr> \
<td colspan="2" class="rounded-foot-left-right"></td></tr></tfoot><tbody><tr><td>Lens Type</td> \
<td>Prime Lens</td></tr><tr><td>Focal Length</td><td>50mm</td></tr><tr><td>Mount Type</td><td>Fujifilm X</tr> \
<tr><td>Format</td><td>APS-C / DX</td></tr><tr><td>Compatible Format(s)</td><td>APS-C</td></tr><tr> \
<td>Compatible with Teleconverters</td><td>No</td></tr><tr><td>Maximum Reproduction Ratio</td><td>0.15x</td> \
</tr><tr><td>Image Stabilization</td><td>No</td></tr><tr><th scope="col" colspan="2">Aperture Information</th> \
</tr><tr><td>Aperture Ring</td><td>Yes</td></tr><tr><td>Maximum Aperture</td><td>f/2</td></tr><tr><td>Minimum Aperture</td> \
<td>f/16</td></tr><tr><td>Maximum Angle of View (APS-C or smaller format)</td><td>31.7°</td></tr><tr> \
<th scope="col" colspan="2">Optical Information</th></tr><tr><td>Lens Elements</td><td>9</td></tr><tr><td>Lens Groups</td> \
<td>7</td></tr><tr><td>Diaphragm Blades</td><td>9 (Rounded)</td></tr><tr><td>Extra-Low Dispersion Glass Elements</td><td>1</td> \
</tr><tr><td>Aspherical Elements</td><td>1</td></tr><tr><td>Nano Coating</td><td>No</td></tr><tr><td>Anti-Reflective Coating</td> \
<td>No</td></tr><tr><th scope="col" colspan="2">Focus Information</th></tr><tr><td>Focus</td><td>Autofocus</td> \
</tr><tr><td>Built-in Focus Motor</td><td>Yes</td></tr><tr><td>Silent Wave / UltraSonic Motor</td><td>No</td></tr> \
<tr><td>Internal Focusing</td><td>Yes</td></tr><tr><td>Minimum Focus Distance</td><td>0.39 m (15.35″)</td></tr><tr> \
<th scope="col" colspan="2">Filter Information</th></tr><tr><td>Filter Size</td><td>46mm</td></tr><tr> \
<td>Accepts Filter Type</td><td>Screw-on</td></tr><tr><th scope="col" colspan="2">Physical Characteristics</th> \
</tr><tr><td>Weather / Dust Sealing</td><td>Yes</td></tr><tr><td>Mount Material</td><td>Metal</td></tr><tr> \
<td>Tripod Collar</td><td>No</td></tr><tr><td>Dimensions</td><td>60.0mm x 59.4mm</td></tr><tr><td>Weight</td> \
<td>200g</td></tr><tr><th scope="col" colspan="2">Other Information</th></tr><tr><td>Available in Colors</td><td>Black</td> \
</tr></tbody></table>'

TESTDATA_DICT_FULL4 = ' \
<table width="100%" id="rounded-corner" summary="Sony FE 100-400mm f/4.5-5.6 GM OSS"><thead> \
<tr><th scope="col" class="rounded-header" width="60%">Lens Specifications</th> \
<th scope="col" align="center"  width="40%" class="rounded-right"></th></tr></thead><tfoot> \
<tr><td colspan="2" class="rounded-foot-left-right"></td></tr></tfoot><tbody><tr><td>Lens Type</td> \
<td>Zoom Lens</td></tr><tr><td>Focal Length</td><td>100-400mm</td></tr><tr><td>Mount Type</td><td>Sony FE</tr> \
<tr><td>Format</td><td>Full Frame / FX</td></tr><tr><td>Compatible Format(s)</td><td>Full Frame / APS-C</td> \
</tr><tr><td>Compatible with Teleconverters</td><td>Yes</td></tr><tr><td>Zoom Ratio</td><td>0.12 - 0.35x</td> \
</tr><tr><td>Maximum Reproduction Ratio</td><td>1:2.85</td></tr><tr><td>Optical SteadyShot / AntiShake (Image Stabilization)</td> \
<td>Yes</td></tr><tr><th scope="col" colspan="2">Aperture Information</th></tr><tr><td>Aperture Ring</td><td>No</td></tr> \
<tr><td>Maximum Aperture</td><td>f/4.5-5.6</td></tr><tr><td>Minimum Aperture</td><td>f/32-40</td></tr> \
<tr><td>Maximum Angle of View (Full Frame format)</td><td>24°</td></tr><tr> \
<th scope="col" colspan="2">Optical Information</th></tr><tr><td>Lens Elements</td><td>22</td> \
</tr><tr><td>Lens Groups</td><td>16</td></tr><tr><td>Diaphragm Blades</td><td>9 (Rounded)</td> \
</tr><tr><td>Extra-Low Dispersion Glass Elements</td><td>2</td></tr><tr><td>Special Glass Elements</td> \
<td>1x Super ED</td></tr><tr><td>Nano AR Coating</td><td>Yes</td></tr><tr> \
<td>Anti-Reflective / Multi-Layered / T* Coating</td><td>No</td></tr><tr><td>Fluorine Coating</td><td>Yes</td></tr> \
<tr><th scope="col" colspan="2">Focus Information</th></tr><tr><td>Focus</td><td>Autofocus</td></tr><tr> \
<td>Built-in Focus Motor</td><td>Yes</td></tr><tr><td>Direct Drive Super Sonic wave Motor (DDSSM)</td><td>No</td> \
</tr><tr><td>Internal Focusing</td><td>Yes</td></tr><tr><td>Minimum Focus Distance</td> \
<td>3.22' + "'" + ' (.98 m)</td></tr><tr><td>Electronic Diaphragm</td><td>Yes</td> \
</tr><tr><th scope="col" colspan="2">Filter Information</th></tr><tr><td>Filter Size</td> \
<td>77mm</td></tr><tr><td>Accepts Filter Type</td><td>Screw-on</td></tr><tr> \
<th scope="col" colspan="2">Physical Characteristics</th></tr><tr> \
<td>Weather / Dust Sealing</td><td>Yes</td></tr><tr><td>Mount Material</td><td>Metal</td></tr> \
<tr><td>Tripod Collar</td><td>Yes</td></tr><tr><td>Dimensions</td> \
<td>Approx. 3.70 x 8.07" (93.9 x 205 mm)</td></tr><tr><td>Weight</td><td>49.21 oz (1395 g)</td> \
</tr><tr><th scope="col" colspan="2">Other Information</th></tr><tr><td>Available in Colors</td><td>Black</td> \
</tr></tbody></table>'


TESTDATA_DICT_FULL5 = ' \
<table width="100%" id="rounded-corner" summary="Sigma 14mm f/1.8 DG HSM Art"><thead><tr> \
<th scope="col" class="rounded-header" width="60%">Lens Specifications</th> \
<th scope="col" align="center"  width="40%" class="rounded-right"></th></tr></thead><tfoot><tr> \
<td colspan="2" class="rounded-foot-left-right"></td></tr></tfoot><tbody><tr><td>Lens Type</td> \
<td>Prime Lens</td></tr><tr><td>Focal Length</td><td>14mm</td></tr><tr><td>Mount Type</td> \
<td>Canon EF, Nikon F, Sigma SA</tr><tr><td>Format</td><td>Full Frame / FX</td></tr><tr><td>Compatible Format(s)</td> \
<td>Full Frame / APS-C</td></tr><tr><td>Compatible with Teleconverters</td><td>No</td></tr> \
<tr><td>Maximum Reproduction Ratio</td><td>1:9.8</td></tr><tr><td>Optical Stabilization (Image Stabilization)</td> \
<td>No</td></tr><tr><th scope="col" colspan="2">Aperture Information</th></tr><tr><td>Aperture Ring</td> \
<td>No</td></tr><tr><td>Maximum Aperture</td><td>f/1.8</td></tr><tr><td>Minimum Aperture</td><td>f/16</td> \
</tr><tr><td>Maximum Angle of View (Full Frame format)</td><td>114.2°</td></tr><tr> \
<th scope="col" colspan="2">Optical Information</th></tr><tr><td>Lens Elements</td><td>16</td></tr><tr> \
<td>Lens Groups</td><td>11</td></tr><tr><td>Diaphragm Blades</td><td>9 (Rounded)</td></tr><tr> \
<td>Low Dispersion Glass Elements</td><td>4</td></tr><tr><td>"F" Low Dispersion Glass Elemenets</td> \
<td>3</td></tr><tr><td>Nano Coating</td><td>No</td></tr><tr><td>Super Multi-Layer Coating</td><td>No</td> \
</tr><tr><th scope="col" colspan="2">Focus Information</th></tr><tr><td>Focus</td><td>Autofocus</td></tr> \
<tr><td>Built-in Focus Motor</td><td>Yes</td></tr><tr><td>Hyper Sonic Motor (HSM)</td><td>Yes</td></tr> \
<tr><td>Internal Focusing</td><td>Yes</td></tr><tr><td>Minimum Focus Distance</td><td>0.27 m (10.63″)</td> \
</tr><tr><th scope="col" colspan="2">Filter Information</th></tr><tr><td>Filter Size</td><td>N/A</td></tr> \
<tr><td>Accepts Filter Type</td><td>Screw-on</td></tr><tr><th scope="col" colspan="2">Physical Characteristics</th> \
</tr><tr><td>Weather / Dust Sealing</td><td>Yes</td></tr><tr><td>Mount Material</td><td>Metal</td></tr> \
<tr><td>Tripod Collar</td><td>No</td></tr><tr><td>Dimensions</td><td>95.4mm x 126mm/9.5in. x 5.0in.</td> \
</tr><tr><td>Weight</td><td>1,170g/41.3oz.</td></tr><tr><th scope="col" colspan="2">Other Information</th> \
</tr><tr><td>Available in Colors</td><td>Black</td></tr></tbody></table>'