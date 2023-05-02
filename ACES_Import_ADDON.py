'''
Copyright (C) 2023 Benjamin Pionczewski
piosbenni@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

'''



bl_info = {
    "name": "Auto ACES Importer",
    "author": "Benjamin Pionczewski",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "View3D > Object Mode > Tool Shelf",
    "description": "Selects the apropriet color space based on signal words, sperate them with ;",
    "warning": "",
    "doc_url": "",
    "category": "Material",
}




import bpy

class IdProperties(bpy.types.PropertyGroup):

    sRGB_id: bpy.props.StringProperty(
        name="sRGB Identifier",
        description=":",
        default="Diff;diff;Col;albedo",
        maxlen=1024,
        )

    HDRi_id: bpy.props.StringProperty(
        name="HDRi Identifier",
        description=":",
        default=".hdr;PANO",
        maxlen=1024,
        )


class OBJECT_OT_ACESImport(bpy.types.Operator):
    bl_idname = "importer.import"
    bl_label = "Import ACES"
    
    def execute(self, context):
        scene = context.scene
        IdProps = scene.IdProps
        
        print(IdProps.sRGB_id)
        print(IdProps.HDRi_id)
        
        sRGB_texture = IdProps.sRGB_id.split(";")
        hdri_texture = IdProps.HDRi_id.split(";")
        for i in sRGB_texture:
            print("Printed: ", i)
        

        
        images = []
        for i in bpy.data.images:
            print (i)
            if i.name !='Render Result' and i.name != 'Viewer Node':
                images.append(i)
        #print(images)
        for i in bpy.data.movieclips:
            images.append(i)
        

        for i in images:
            if any(x in i.name for x in sRGB_texture):
                print("sRGB: ",i)
                i.colorspace_settings.name = 'Utility - sRGB - Texture'
            elif any(x in i.name for x in hdri_texture):
                print("HDRI: ", i)
                i.colorspace_settings.name = 'Utility - Linear - sRGB'
    
            else:
                print("Raw: ", i)
                i.colorspace_settings.name = 'Utility - Raw'
        
        
        return {'FINISHED'}
        

        


class PANEL_PT_ACESImportToolsPanel(bpy.types.Panel):
    bl_label = "ACES Importer"
    bl_idname = "PANEL_PT_ACESImportToolsPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ACES_Importer"
 
    def draw(self, context):
        scene = context.scene
        IdProps = scene.IdProps
        
        self.layout.prop(IdProps, "sRGB_id")
        self.layout.prop(IdProps, "HDRi_id")
        self.layout.operator("importer.import")
        
        
        
        
        
classes =(
IdProperties,
OBJECT_OT_ACESImport,
PANEL_PT_ACESImportToolsPanel
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.IdProps = bpy.props.PointerProperty(type=IdProperties)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.IdProps

if __name__ == "__main__":
    register()
