import bpy
from bpy.props import BoolProperty, EnumProperty, FloatProperty, PointerProperty

from ..generic import SizeOffsetProperty
from ..rails import RailProperty


class BalconyProperty(bpy.types.PropertyGroup):
    redo: BoolProperty()

    width: FloatProperty(
        name="Balcony Width",
        min=0.01,
        max=100.0,
        default=1.2,
        description="Width of balcony",
    )

    railing: BoolProperty(
        name="Add Railing", default=True, description="Whether the balcony has railing"
    )

    open_items = [
        ("NONE", "None", "", 0),
        ("FRONT", "Front", "", 1),
        ("LEFT", "Left", "", 2),
        ("RIGHT", "Right", "", 3),
    ]

    open_side: EnumProperty(
        name="Open Side",
        items=open_items,
        default="NONE",
        description="Sides of the balcony with no railing",
    )

    rail: PointerProperty(type=RailProperty)
    size_offset: PointerProperty(type=SizeOffsetProperty)

    def set_defaults(self):
        """ Helper function to make convinient property adjustments """
        if self.redo:
            return

        self.size_offset.size = (0.5, 1.0)
        self.redo = True

    def draw(self, context, layout):
        self.size_offset.draw(context, layout)

        row = layout.row()
        row.prop(self, "width")

        layout.prop(self, "railing", toggle=True)
        if self.railing:
            box = layout.box()
            box.prop_menu_enum(self, "open_side", text="Open")
            self.rail.draw(context, box)
