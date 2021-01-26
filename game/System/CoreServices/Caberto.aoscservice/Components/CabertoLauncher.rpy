#
# CabertoLauncher.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

screen CabertoLauncher(apps):
    tag desktop
    modal False
    style_prefix "CabertoLauncher"
    
    frame:
        yfill True
        xsize 72
        
        has vbox:
            xalign 0.5
            yalign 1.0
            yanchor 1.0
            
            vbox:
                box_reverse True
                
                for app in apps:
                    python:
                        _icon = app.get_app_icon(64) if isinstance(app, CAApplication) else app.icons[64]
                        _name = app.product_name if isinstance(app, CAApplication) else app.bundleName
                
                    button action Function(app.application_will_launch):
                        xysize (72, 72)
                        add _icon:
                            xalign 0.5
                                
            button action Function(caberto.drawer):
                ysize 72
                add "#FC9856" # TODO: Replace this with the Caberto/Candella logo.
                add caberto.bundleDir + "Resources/distributor_logo.png":
                    align (0.5, 0.5)
        
style CabertoLauncher_frame is frame:
    margin (0, 0)
    padding (0, 0)
    background "#212121EE"