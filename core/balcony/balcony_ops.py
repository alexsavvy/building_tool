import bpy
from .balcony import Balcony
from .balcony_props import BalconyProperty


class BTOOLS_OT_add_balcony(bpy.types.Operator):
    """Create a balcony from selected faces"""

    bl_idname = "btools.add_balcony"
    bl_label = "Add Balcony"
    bl_options = {"REGISTER", "UNDO"}

    props: bpy.props.PointerProperty(type=BalconyProperty)

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.mode == "EDIT_MESH"

    def execute(self, context):
        self.props.set_defaults()
        return Balcony.build(context, self.props)

    def draw(self, context):
        self.props.draw(context, self.layout)
