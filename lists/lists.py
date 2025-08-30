import itertools
from utils.string_utils import get_capitalisation_variants
import string

separators = ["", " ", "_", "-"]

found_track_names = [
    "AI_output",
    "Blink_output",
    "BMP_output",
    "CH_output",
    "chin_raiser_bs",
    "EE_output",
    "Eyebrow Raise_output",
    "Frown_output",
    "FV_output",
    "Head_Pitch_Pos",
    "Head_Roll_Pos",
    "Head_Yaw_Pos",
    "jaw_open_bs",
    "lips_funnel_bs",
    "lips_funnel",
    "lips_smile_l_bs",
    "mouthDn_output",
    "mouthUp_output",
    "OO_output",
    "open_output",
    "Rest Pose",
    "sneer_l_bs",
    "Sneer_output",
    "sneer_r_bs",
    "squint_l_bs",
    "Squint_output",
    "squint_r_bs",
    "tBack_output",
    "tRoof_output",
    "tTeeth_output",
]

found_bone_names = [
    "brow_01_l",
    "brow_01_r",
    "brow_02_l",
    "brow_02_r",
    "brow_03_l",
    "brow_03_r",
    "brow_04_l",
    "brow_04_r",
    "chin_m_01",
    "eyebrow_l_04",
    "eyebrow_r_04",
    "gullet_m_01",
    "gullet_m_02",
    "jaw_m",
    "lower_cheek_l",
    "lower_cheek_r",
    "nose_l_01",
    "nose_l_02",
    "nose_l_03",
    "nose_l_04",
    "nose_m",
    "nose_m_01",
    "nose_r_01",
    "nose_r_02",
    "nose_r_03",
    "nose_r_04",
    "nosebridge_m_01",
    "nosebridge_m_02",
    "nosebridge_m_03",
    "nosetip_m_01",
    "nosetip_m_02",
    "sneer_l_01",
    "sneer_l_02",
    "sneer_r_01",
    "sneer_r_02",
    "tongue_04",
]

docs_track_names = [
    "PBM",
    "ShCh",
    "Rest Pose",
    "BrowAngry",
    "Head_Pitch_Pos",
    "Head_Yaw_Pos",
    "Head_Roll_Pos",
    "LeftEye_Pitch_Pos",
    "LeftEye_Yaw_Pos",
    "RightEye_Pitch_Pos",
    "RightEye_Yaw_Pos",
    "Head_Pitch_Neg",
    "Head_Yaw_Neg",
    "Head_Roll_Neg",
    "LeftEye_Pitch_Neg",
    "LeftEye_Yaw_Neg",
    "RightEye_Pitch_Neg",
    "RightEye_Yaw_Neg",
    "Look_Up_Lids",
    "Look_Down_Lids",
    "Eyes_Yaw_Neg",
    "Eyes_Yaw_Pos",
    "Eyes_Pitch_Pos",
    "Eyes_Pitch_Neg",
    "Mouth_Sad",
    "Mouth_Anger",
    "Mouth_Happy",
    "Mouth_Snarl",
    "Mouth_Pain",
    "Mouth_Pout",
    "Brows_Sad",
    "Brows_Anger",
    "Brows_Happy",
    "Brows_Pain",
    "CDGKNRSTh",
    "CDGKNRS",
    "CDGKNS",
    "CDGKN",
    "input",
]

extra_body_parts = [
    "neck",
    "brow",
    # "shoulder",
    "eye",
    "nose",
    "forehead",
    "tongue",
    "palate",
    "jaw",
    # "philtrum",
    # "larynx",
    "teeth",
    "chin",
    "lid",
    "bone",
]

extra_directions = [
    "in",
    "out",
    "up",
    "down",
    "left",
    "right",
    "high",
    "forward",
    "fw",
    "backward",
    "back",
    "bk",
    "raise",
    "lower",
    "lowerer",
    "open",
    "close",
    "closed",
    "center",
    "centre",
    "central",
]

extra_poses = [
    "Frown",
    "Smile",
    "Surprise",
    "Neutral",
    "wrinkle",
    "pout",
    "smirk",
]

ipa = [
    "p",
    "b",
    "t",
    "d",
    "k",
    "g",
    "m",
    "n",
    "ŋ",
    "tʃ",
    "ʃ",
    "dʒ",
    "ʒ",
    "f",
    "v",
    "θ",
    "ð",
    "s",
    "z",
    "ʃ",
    "ʒ",
    "h",
    "w",
    "j",
    "r",
    "l",
    "i",
    "ɪ",
    "e",
    "ɛ",
    "æ",
    "ʌ",
    "ə",
    "u",
    "ʊ",
    "oʊ",
    "ɔ",
    "ɑ",
    "aɪ",
    "ɪ",
    "aʊ",
    "a",
    "ʊ",
    "ɔɪ",
    "ɔ",
    "ɪ",
    "x",
    "ʔ",
]

lower_case_letters = list(string.ascii_lowercase)
numbers = [str(i) for i in range(15)]
numbers_with_leading_zero = [f"0{i}" for i in range(10)]

extras_no_cap_variants = (
    ["", "s", "/"]
    + extra_directions
    + extra_body_parts
    + extra_poses
    # + numbers
    # + numbers_with_leading_zero
    # + lower_case_letters
    # + ipa
)

extras_cap_variants = list(
    itertools.chain.from_iterable(
        get_capitalisation_variants(extra) for extra in extras_no_cap_variants
    )
)

extras = extras_cap_variants
