import bpy
from .rails import Rails
from .rails_props import RailProperty


class BTOOLS_OT_add_railing(bpy.types.Operator):
    """Add railing to selected upward facing faces"""

    bl_idname = "btools.add_railing"
    bl_label = "Add Railing"
    bl_options = {"REGISTER", "UNDO"}

    props: bpy.props.PointerProperty(type=RailProperty)

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.mode == "EDIT_MESH"

    def execute(self, context):
        return Rails.build(context, self.props)

    def draw(self, context):
        self.props.draw(context, self.layout)
