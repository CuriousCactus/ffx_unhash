import itertools
from utils.string_utils import get_capitalisation_variants
import string

separators = ["", " ", "_", "-"]

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
