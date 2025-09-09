import re

page = """Bone Collections

Bone Collections group the bones of an Armature into named collections. The armature is the owner of these collections, so they are available in all modes. Bone Collections are identified by their name, which are unique within the Armature. Bone Collections can be nested inside other Bone Collections to create an organized hierarchy for complex rigs.

In the text below, “collection” is understood to refer to “bone collection”; Scene Collections are not described here.

Bone Collections can be managed via the Armature and Bone property panels.
Visibility

Bone Collections can be shown & hidden via the list in the Armature properties, as well as via the list in the Bone properties. Bone visibility is determined by the visibility of its collections, its own ‘solo’ and ‘hidden’ properties:

    If the bone itself is marked as ‘hidden’, it is invisible regardless of the bone collections.

    If a parent collection is hidden, child collections will also be hidden; same is true for soloed collections.

    A bone is visible when it is contained in any visible collection.

    If a collection is soloed, it will be visible regardless of the collection’s ‘hidden’ property.

    A bone that is not assigned to any bone collection is visible; otherwise it would be impossible to select it & assign it to a collection.

Library Overrides

Bone collections can be added using library overrides. For this to work, both the armature Object and the Armature itself need to be overridden.
Limitations

There are a few limitations when it comes to bone collections & overrides:

    Only bone collections that are local to the current blend file can be edited.

    Bone collections that already existed on the linked-in Armature are read-only, and only their visibility can be toggled. Those visibility changes won’t be saved, though.

    Custom properties of overridden bone collections cannot be edited in the properties panel. Python access is fine; this is just a current limitation of Blender’s UI code.

How It Works

Bone collections added via overrides are ‘anchored’ to the preceding collection, by name. Here is an example. The italic collections are defined on the linked Armature in armature.blend. The bold ones are added by overrides in armature_shot_47.blend.

    FK Controls

    IK Controls

    Left Pinky (anchored to “IK Controls”)

    Right Pinky (anchored to “Left Pinky”)

Now if the Armature in armature.blend gets updated with two more collections it might look like this:

    FK Controls

    IK Controls

    Face Controls

    Face Detail Controls

After reloading armature_shot_47.blend, it will look like this:

    FK Controls

    IK Controls

    Left Pinky (still anchored to “IK Controls”)

    Right Pinky (still anchored to “Left Pinky”)

    Face Controls

    Face Detail Controls

Some history
Bone Collections were introduced in Blender 4.0, as a replacement for armature layers and bone groups. Bone Collections are owned by the Armature, so they are available in all modes. To contrast, bone groups were stored on the object’s pose, and thus were not available in armature edit mode.

Much like in real-life skeletons, Bones are the building blocks of Armatures. Each bone has a resting position, orientation, and length – and all of these can be changed while posing or animating.

You can change the way bones are displayed in the armature’s Viewport Display settings.
Classification

Bones can be classified into two types depending on their Deform setting:
Deforming Bones

Bones that have the Deform setting enabled will drag vertices along with them. For example, you could have a bone in a character’s upper arm and another in the lower arm, and then rotate and flex the arm by transforming these bones.
Control Bones

Bones that have the Deform setting disabled do not drag any vertices along. Instead, they’re typically used to control other bones.

A common use case is inverse kinematics: rotating the above two arm bones manually is a bit of a pain, so instead, you can add a control bone and configure the arm bones to automatically orient themselves towards it. This way, you can simply position the control bone where the character’s hand should be, which is much easier.


Copy Location Constraint

The Copy Location constraint forces its owner to have the same location as its target.

Important

Note that if you use such a constraint on a connected bone, it will have no effect, as it is the parent’s tip which controls the position of your owner bone’s root.
Options
../../../_images/animation_constraints_transform_copy-location_panel.png

Copy Location panel.

Target

    Data ID used to select the constraints target, and is not functional (red state) when it has none. See common constraint properties for more information.
Axis

    These buttons control which axes are constrained.
Invert

    Invert their respective corresponding axis coordinates.
Offset

    When enabled, this control allows the owner to be moved (using its current transform properties), relative to its target’s position.
Target/Owner

    Standard conversion between spaces. See common constraint properties for more information.
Influence

    Controls the percentage of affect the constraint has on the object. See common constraint properties for more information.

Examples
Animation

Let us animate a solar system with the Copy Location constraint and its Offset option. You can make the owner, called “moon”, describe perfect circles centered on the world origin (using e.g. Location X/Y sine and cosine F-Curves, see Built-in Function Modifier). Then copy the location of a target “earth” with the Offset checkbox enabled to model a satellite in a (simplified) orbit around its planet. Repeat these steps for more planets circling around its center star “sun”.

Following video is a small animation of a solar system created using (among a few others) the previously described technique:

Note that, this ‘solar’ system is not realistic at all (the wrong scale, the earth is rotating in the wrong direction around the sun, …).

You can download the blend-file used to create this animation.

Furthermore you can also animate a few properties of each constraint using animation curves: e.g. you can animate the Influence of a constraint. It is used to first let the camera follow the moon, then the earth, and finally using two Copy Location constraints with Offset set.

Bendy Bones (B-Bones) are an easy way to replace long chains of many small rigid bones. A common use case for curved bones is to model spine columns or facial bones.
Technical Details

Blender treats the bone as a section of a Bézier curve passing through the bones’ joints. Each of the Segments will bend and roll to follow this invisible curve representing a tessellated point of the Bézier curve. The control points at each end of the curve are the endpoints of the bone. The shape of the B-Bones can be controlled using a series of properties or indirectly through the neighboring bones (i.e. first child and parent). The properties construct handles on either end of the bone to control the curvature.

When using the B-bone as a constraint target Data ID offers an option to follow the curvature.

Note

However, if the bone is used as a target rather than to deform geometry, only Armature and Copy Transforms constraints will use the full transformation including roll and scale.
Display

You can see these segments only if bones are visualized as B-bones.

When not visualized as B-Bones, bones are always shown as rigid sticks, even though the bone segments are still present and effective. This means that even in e.g. Octahedron visualization, if some bones in a chain have several segments, they will nonetheless smoothly deform their geometry.
Rest Pose

The initial shape of a B-Bone can be defined in Edit Mode as a rest pose of that bone. This is useful for curved facial features like curved eyebrows or mouths.

B-Bones have two sets of the Bendy Bone properties – one for Edit Mode (i.e. the Rest Pose/Base Rig) and another for Pose Mode – adding or multiplying together their values to get the final transforms.
Example
../../../../_images/animation_armatures_bones_properties_bendy-bones_b-bones-1.png

Bones with just one segment in Edit Mode.
../../../../_images/animation_armatures_bones_properties_bendy-bones_b-bones-2.png

The Bézier curve superposed to the chain, with its handles placed at bones’ joints.
../../../../_images/animation_armatures_bones_properties_bendy-bones_b-bones-3.png

The same armature in Object Mode.

In Fig. Bones with just one segment in Edit Mode. we connected three bones, each one made of five segments.

Look at Fig. The same armature in Object Mode., we can see how the bones’ segments smoothly “blend” into each other, even for roll.
../../../../_images/animation_armatures_bones_properties_bendy-bones_pose-mode.png

An armature in Pose Mode, B-Bone visualization: Bone.003 has one segment, Bone.004 has four, and Bone.005 has sixteen.
Options
../../../../_images/animation_armatures_bones_properties_bendy-bones_options.png

Bendy Bones panel.

Segments

    The number of segments, which the given bone is subdivided into. Segments are small, rigid linked child bones that interpolate between the root and the tip. The higher this setting, the smoother “bends” the bone, but the heavier the pose calculations.

Display Size X, Z

    Controls the visible thickness of the bone segments when the armature is rendered in the B-Bones mode.

Vertex Mapping

    Controls how vertices are weighted to the individual segments of a B-Bone for deformations:

    Straight:

        A fast mapping that works well for B-Bones with a straight or gently curved rest pose.
    Curved:

        A slower mapping that improves deformations for B-Bones with a strongly curved rest pose. This should be used selectively when needed.

    ../../../../_images/animation_armatures_bones_properties_bendy-bones_vertex-mapping.png

    Straight vs Curved vertex mapping on a B-Bone with a strongly curved rest pose.

Curve In/Out X, Y, Z

    Applies offsets to the curve handle positions on the plane perpendicular to the bone’s primary (Y) axis. As a result, the handle moves per axis (XZ) further from its original location, causing the curve to bend.

Roll In, Out

    The roll value (or twisting around the main Y axis of the bone) is interpolated per segment, between the start and end roll values. It is applied as a rotational offset on top of the rotation defined by the handle bones.

Inherit End Roll

    If enabled, the Roll Out value of the Start Handle bone (connected parent by default) will be implicitly added to the Roll In setting of the current bone.

Scale In/Out X, Y, Z

    Scaling factors that adjust the thickness of each segment for the X and Z axes, or introduce non-uniform spacing along the Y axis. Similar to Roll it is interpolated per segment.

    Since all segments are still uniformly scaled in the Y direction to fit the actual length of the curve, only the ratio between Scale In Y and Scale Out Y actually matters.

Ease In, Out

    The Ease In/Out number fields, change the “length” of the “auto” Bézier handle to control the “root handle” and “tip handle” of the bone, respectively. These values are proportional to the default length, which of course automatically varies depending on bone length, angle with the reference handle, and so on.

    Although easing is a scale-like value, the Edit Mode and Pose Mode versions of the values are added, so they get corresponding start values of 1 and 0 by default.
    Ease In/Out settings example, with a materialized Bézier curve.

../../../../_images/animation_armatures_bones_properties_bendy-bones_curve-in-out-1.png

Bone.004 with default In and Out (1.0).
../../../../_images/animation_armatures_bones_properties_bendy-bones_curve-in-out-2.png

Bone.004 with In at 2.0, and Out at 0.0.

Scale Easing

    If enabled, the final easing values are implicitly multiplied by the corresponding Scale Y values.

Custom Handles

B-Bones can use custom bones as their reference bone handles, instead of only using the connected parent/child bones.

Start/End Handle

    Specifies the type of the handle from the following choices:

    Automatic:

        The connected parent (or first connected child) of the bone is chosen as the handle. Calculations are done according to the Absolute handle type below.
    Absolute:

        The Bézier handle is controlled by the position of the head (tail) of the handle bone relative to the head (tail) of the current bone. Note that for this to work, there must be a nonzero distance between these bones. If the handle is also a B-Bone, additional processing is applied to further smooth the transition, assuming that the bones in effect form a chain.
    Relative:

        The Bézier handle is controlled by the offset of the head (tail) of the handle bone from its rest pose. The use of this type is not recommended due to numerical stability issues near zero offset.
    Tangent:

        The Bézier handle is controlled by the orientation of the handle bone, independent of its location.

Custom Handle

    For types other than Automatic, a bone to use as handle has to be manually selected. Switching to a custom handle type without selecting a bone can be used to effectively disable the handle.

    It is valid for two bones to refer to each other as handles – this correlation is applied in connected chains with Automatic handles.

Scale X/Y/Z/Ease

    If enabled, the final Scale and/or Ease values are multiplied by the corresponding local scale channels of the handle bone. This step is applied independently of Scale Easing and doesn’t interact with it, i.e. enabling Y and Scale Easing doesn’t replace the Ease toggle. These toggles are a more efficient replacement for up to eight trivial drivers passing segment scale data from the handle bones into the B-Bone option properties.

Tip

Keying Set

The “BBone Shape” Keying Set includes all Bendy Bones properties.
../../../../_images/animation_armatures_bones_properties_bendy-bones_settings-demo.png

Visualization of the Bendy Bones properties.

From Left: 1) Curve X/Y offsets, 2) Scale In/Out, 3) Roll In/Out


"""

blender_docs_words = list(sorted([word.lower() for word in list(set(re.split("[ é/…:;_&\(\)\-’‘“”,\.\n]", page)))]))