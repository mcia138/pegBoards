# auto generated
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split,SplitSide,SplitType
keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[18,209,123],[255,0,0],[55,55,55],[55,55,55],[55,55,55],[55,55,55]],split=False,rightSide=False,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)

# keymap
keyboard.keymap=[ [KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,KC.Y,KC.U,KC.I,KC.O,KC.P,KC.BSPC,KC.LCTL,KC.A,KC.S,KC.D,KC.F,KC.G,KC.H,KC.J,KC.K,KC.L,KC.SCLN,KC.QUOT,KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,KC.N,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.NO,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.NO,KC.NO,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINS,KC.EQL,KC.LCBR,KC.RCBR,KC.PIPE,KC.GRV,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDS,KC.PLUS,KC.LBRC,KC.RBRC,KC.BSLS,KC.TILD,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINS,KC.EQL,KC.LCBR,KC.RCBR,KC.PIPE,KC.GRV,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDS,KC.PLUS,KC.LBRC,KC.RBRC,KC.BSLS,KC.TILD,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINS,KC.EQL,KC.LCBR,KC.RCBR,KC.PIPE,KC.GRV,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDS,KC.PLUS,KC.LBRC,KC.RBRC,KC.BSLS,KC.TILD,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINS,KC.EQL,KC.LCBR,KC.RCBR,KC.PIPE,KC.GRV,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDS,KC.PLUS,KC.LBRC,KC.RBRC,KC.BSLS,KC.TILD,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINS,KC.EQL,KC.LCBR,KC.RCBR,KC.PIPE,KC.GRV,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDS,KC.PLUS,KC.LBRC,KC.RBRC,KC.BSLS,KC.TILD,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI],
[KC.ESC,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.LPRN,KC.RPRN,KC.BSPC,KC.LCTL,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.MINS,KC.EQL,KC.LCBR,KC.RCBR,KC.PIPE,KC.GRV,KC.LSFT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.UNDS,KC.PLUS,KC.LBRC,KC.RBRC,KC.BSLS,KC.TILD,KC.LALT,KC.MO(1),KC.SPC,KC.MO(2),KC.RGUI]]
# keymap
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)
