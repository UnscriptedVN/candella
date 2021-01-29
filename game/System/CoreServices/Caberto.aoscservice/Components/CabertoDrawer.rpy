#
# CabertoDrawer.rpy
# Caberto Desktop Shell
#
# (C) 2021 Marquis Kurt. All rights reserved.
#

init screen CabertoDrawer():
    style_prefix "CabertoDrawer"
    modal False
        
    $ all_apps = caberto.get_all_applications()
    
    frame:
        xsize 700
        yfill True
        
        has vbox:
            spacing 48
            
            # TODO: Put a search bar here.
            # text "Search..."
            
            hbox:
                box_wrap True
                
                for app in all_apps:
                    python:
                        _app_name = app.get_name() if isinstance(app, CAApplication) else app.bundleName
                            
                        if len(_app_name) > 36:
                            _app_name = _app_name[:34] + "..."
                    
                    button action [
                        Function(caberto.drawer), Function(caberto.launch_app_bundle, app_bundle=app)
                    ]:
                        xysize(96, 72)
                        sensitive True
                        
                        vbox:
                            xfill True
                            yfill True
                            
                            add app.icons[64]:
                                xalign 0.5
                            text "[_app_name]":
                                xalign 0.5
                                text_align 0.5
        

                                    
style CabertoDrawer_frame is frame:
    margin (0, 0)
    top_margin 28
    left_margin 72
    padding(24, 16)
    background "#080808EE"
    
style CabertoDrawer_text is ASSystemRegularFont:
    size 16
