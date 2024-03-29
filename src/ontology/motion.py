from owlready2 import *

onto = get_ontology("http://www.ease-crc.org/ont/mixing")

with onto:
    class Motion(Thing):
        label = [locstr("motion", "en")]


    class hasMotion(ObjectProperty, Motion >> Motion):
        pass


    class followedBy(ObjectProperty, Motion >> Motion):
        pass


    class motion_parameters(DataProperty, Motion >> float):
        pass


    class angle_shift1(motion_parameters):
        pass


    class angle_shift2(motion_parameters):
        pass


    class height_increment(motion_parameters):
        pass


    class radius_lower_bound_absolute(motion_parameters):
        pass


    class radius_upper_bound_absolute(motion_parameters):
        pass


    class radius_lower_bound_relative(motion_parameters):
        pass


    class radius_upper_bound_relative(motion_parameters):
        pass


    class vertical_increment(motion_parameters):
        pass


    class MixingMotion(Motion):
        label = [locstr("mixing motion", "en")]


    class CircularDivingToInnerMotion(MixingMotion):
        label = [locstr("circular diving to inner motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7),
                height_increment.value(0.1)]


    class CircularMotion(MixingMotion):
        label = [locstr("circular motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.8) & radius_upper_bound_relative.value(0.7)]


    class FoldingMotion(MixingMotion):
        label = [locstr("folding motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7),
                angle_shift1.value(90), angle_shift2.value(22.5)]


    class VerticalCircularMotion(MixingMotion):
        label = [locstr("vertical circular motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7),
                vertical_increment.value(0.1)]


    class WhirlstormMotion(MixingMotion):
        label = [locstr("whirlstorm motion", "en")]
        is_a = [radius_lower_bound_relative.value(0.0) & radius_upper_bound_relative.value(0.7)]


    class CompoundMotion(Motion):
        label = [locstr("compound motion", "en")]


    class WhirlstormThenCircularDivingToInner(CompoundMotion):
        label = [locstr("whirlstorm then circular to diving inner")]
        equivalent_to = [Motion & (hasMotion.some(WhirlstormMotion & followedBy.some(CircularDivingToInnerMotion)
                                                  & followedBy.exactly(1, Motion)))]


    class WhirlstormThenVertical(CompoundMotion):
        label = [locstr("whirlstorm then vertical")]
        equivalent_to = [Motion & (hasMotion.some(WhirlstormMotion & followedBy.some(VerticalCircularMotion) &
                                                  followedBy.exactly(1, Motion)))]
