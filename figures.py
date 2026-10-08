import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Liberation Serif", "DejaVu Serif"],
    "font.size": 10,
})
OUT = ""
INK, GRAY, LIGHT = "#1a1a1a", "#6e6e6e", "#b5b5b5"
BLUE, ORANGE = "#4472C4", "#ED7D31"


def box(ax, x, y, w, h, text, fs=9.2, ec=INK, lw=1.4, fc="white", tc=INK, ls="solid"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                 boxstyle="round,pad=0.012,rounding_size=0.02",
                 fc=fc, ec=ec, lw=lw, linestyle=ls, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs,
            fontweight="bold", color=tc, zorder=4)


def arrow(ax, p1, p2, color=INK, lw=1.7, ls="-", rad=0.0, ms=14):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=ms,
                 color=color, lw=lw, linestyle=ls, shrinkA=2, shrinkB=2,
                 connectionstyle=f"arc3,rad={rad}", zorder=2))


# ============================================================ FIGURE 1  curve
fig, ax = plt.subplots(figsize=(5.0, 3.15))
x = np.linspace(0, 3, 400)
C, FLOOR, k = 6.0, 1.6, 1.9
ax.plot(x, FLOOR + (C - FLOOR) * np.exp(-k * x), color=INK, lw=2.2, zorder=4)

ax.axhline(FLOOR, color=GRAY, ls="--", lw=1.1, zorder=2)
ax.annotate("Conceptual floor: baseline purchasing from\nplanned trips, which proximity cannot remove",
            xy=(2.25, FLOOR), xytext=(1.0, 0.25), fontsize=8.5, color=GRAY, ha="left",
            arrowprops=dict(arrowstyle="->", color=GRAY, lw=0.9))
ax.axhline(0, color=LIGHT, ls=":", lw=1.1, zorder=2)
ax.text(0.02, -0.72, "measurement floor at 0: a false floor, where non-purchasing households pile up",
        fontsize=8, color=LIGHT, ha="left", va="center", style="italic")

ax.plot([0], [C], "o", color=INK, ms=6, zorder=5)
ax.annotate("Constant (y-intercept) = ceiling. Even at zero\ndistance, purchasing is capped by household\nbudget and by physiology.",
            xy=(0, C), xytext=(0.72, 6.95), fontsize=8.5, color=INK,
            arrowprops=dict(arrowstyle="->", color=INK, lw=0.9))
ax.annotate("steep decline: crossing from\n\"already on my route\" to\n\"a dedicated trip\"",
            xy=(0.33, 3.75), xytext=(0.78, 4.35), fontsize=8.5, color="#8a6d1f",
            arrowprops=dict(arrowstyle="->", color="#8a6d1f", lw=1.1))
ax.text(1.62, 2.45, "flattening: beyond this, extra distance\nadds little, the trip is already deliberate",
        fontsize=8.5, color=GRAY)

ax.set_xlabel("Network distance to nearest off-premise alcohol outlet (miles)")
ax.set_ylabel("Alcohol spending as % of monthly household income")
ax.set_xlim(-0.08, 3.05); ax.set_ylim(-1.05, 7.7)
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(GRAY)
ax.tick_params(colors=GRAY, labelsize=9)
fig.tight_layout()
fig.savefig(OUT + "Figure1_operational_linkage.png", dpi=300)
plt.close(fig)

# ========================================================= FIGURE 2  spurious
fig, ax = plt.subplots(figsize=(5.0, 2.66))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
box(ax, 0.50, 0.85, 0.36, 0.18, "Vehicle access  (Z)")
box(ax, 0.17, 0.33, 0.30, 0.20, "Network distance\nto nearest outlet\n(X)")
box(ax, 0.83, 0.33, 0.30, 0.20, "Alcohol spending\nshare of income\n(Y)")

arrow(ax, (0.40, 0.76), (0.21, 0.44))
ax.text(0.26, 0.62, "+", fontsize=14, color=INK, ha="center")
ax.text(0.015, 0.60, "car owners can live in\nlower-density areas,\nso outlets are farther",
        fontsize=8.2, color=GRAY, ha="left", va="center")

arrow(ax, (0.60, 0.76), (0.79, 0.44))
ax.text(0.74, 0.62, "–", fontsize=14, color=INK, ha="center")
ax.text(0.985, 0.60, "a car reaches bulk and\ndiscount retail, lowering\nprice paid per drink",
        fontsize=8.2, color=GRAY, ha="right", va="center")

ax.add_patch(FancyArrowPatch((0.33, 0.33), (0.67, 0.33), arrowstyle="-", lw=1.6,
             color=LIGHT, linestyle=(0, (5, 3)), shrinkA=3, shrinkB=3, zorder=2))
ax.text(0.50, 0.265, "observed negative association,\npossibly artifact", fontsize=8.4,
        color=GRAY, ha="center", va="top", style="italic")
ax.text(0.50, 0.055, "Z produces X and Y independently, reproducing the very sign the theory predicts.",
        ha="center", fontsize=8.6, color=GRAY)
fig.tight_layout()
fig.savefig(OUT + "Figure2_spurious.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ======================================================== FIGURE 3  mediation
fig, axes = plt.subplots(1, 2, figsize=(6.3, 2.18))
for ax in axes:
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

a = axes[0]
a.text(0.5, 0.95, "Does not work: Z as mediator", ha="center", fontsize=11,
       fontweight="bold", color=GRAY)
box(a, 0.15, 0.52, 0.24, 0.20, "Distance\n(X)", fs=9, ec=LIGHT, tc=GRAY)
box(a, 0.50, 0.52, 0.26, 0.20, "Vehicle\naccess (Z)", fs=9, ec=LIGHT, tc=GRAY, ls=(0, (4, 3)))
box(a, 0.85, 0.52, 0.24, 0.20, "Spending\n(Y)", fs=9, ec=LIGHT, tc=GRAY)
arrow(a, (0.28, 0.52), (0.36, 0.52), color=LIGHT, lw=1.3)
arrow(a, (0.64, 0.52), (0.72, 0.52), color=LIGHT, lw=1.3)
a.plot([0.28, 0.36], [0.60, 0.44], color="#b03a2e", lw=2.0, zorder=6)
a.plot([0.28, 0.36], [0.44, 0.60], color="#b03a2e", lw=2.0, zorder=6)
a.text(0.5, 0.21, "How far the store is does not cause a\nhousehold to own a car. Time order fails.",
       ha="center", fontsize=8.6, color=GRAY, style="italic")

b = axes[1]
b.text(0.5, 0.95, "Works instead: Z at the front", ha="center", fontsize=11,
       fontweight="bold", color=INK)
box(b, 0.15, 0.52, 0.26, 0.20, "Vehicle\naccess (Z)", fs=9)
box(b, 0.50, 0.52, 0.30, 0.20, "Physical\naccessibility (X)", fs=9)
box(b, 0.85, 0.52, 0.24, 0.20, "Spending\n(Y)", fs=9)
arrow(b, (0.28, 0.52), (0.35, 0.52))
arrow(b, (0.65, 0.52), (0.73, 0.52))
b.text(0.315, 0.63, "–", fontsize=13, color=INK, ha="center")
b.text(0.69, 0.63, "–", fontsize=13, color=INK, ha="center")
b.text(0.5, 0.21, "The independent variable becomes the mediator.\nHolds for the concept, not for distance in miles.",
       ha="center", fontsize=8.6, color=GRAY, style="italic")
fig.tight_layout()
fig.savefig(OUT + "Figure3_mediation.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ======================================================= FIGURE 4  moderation
fig, ax = plt.subplots(figsize=(4.4, 2.05))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
box(ax, 0.17, 0.33, 0.30, 0.24, "Network distance\nto nearest outlet\n(X)")
box(ax, 0.83, 0.33, 0.30, 0.24, "Alcohol spending\nshare of income\n(Y)")
box(ax, 0.50, 0.86, 0.30, 0.19, "Vehicle access  (Z)")
arrow(ax, (0.33, 0.33), (0.67, 0.33), lw=2.0)
ax.text(0.50, 0.21, "–", fontsize=15, color=INK, ha="center")
arrow(ax, (0.50, 0.755), (0.50, 0.46), lw=1.8)
ax.text(0.53, 0.60, "moderates", fontsize=9, style="italic", color=INK, ha="left")
ax.text(0.50, 0.05, "No sign is placed on the moderation arrow.", ha="center",
        fontsize=8.4, color=GRAY, style="italic")
fig.tight_layout()
fig.savefig(OUT + "Figure4_moderation.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ======================================================== FIGURE 5  bar chart
fig, ax = plt.subplots(figsize=(4.9, 3.22))
labels = ["Near\n(within 0.5 miles)", "Far\n(more than 0.5 miles)"]
no_veh, has_veh = [6.0, 2.8], [3.0, 2.6]
xpos = np.array([0.0, 1.4]); w = 0.32
ax.bar(xpos - w / 2, no_veh, w, label="No vehicle", color=BLUE, zorder=3)
ax.bar(xpos + w / 2, has_veh, w, label="Has vehicle", color=ORANGE, zorder=3)

ax.plot(xpos - w / 2, no_veh, "o-", color=INK, ms=8, lw=1.6, zorder=5)
ax.plot(xpos + w / 2, has_veh, "o-", color=INK, ms=8, lw=1.6, zorder=5)
ax.text(0.70, 4.75, "steep slope:\ndistance matters", fontsize=9.5, color=INK,
        style="italic", ha="center")
ax.text(0.70, 1.85, "shallow slope:\ndistance matters little", fontsize=9.5, color=INK,
        style="italic", ha="center")

ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=10)
ax.set_xlim(-0.6, 2.0)
ax.set_ylabel("Alcohol spending as % of monthly income")
ax.set_xlabel("Distance to nearest off-premise alcohol outlet")
ax.set_title("Distance and alcohol spending share,\nby household vehicle access", fontsize=12, pad=12)
ax.set_ylim(0, 7.2)
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(GRAY)
ax.tick_params(colors=GRAY)
ax.yaxis.grid(True, color="#E4E2E8", lw=0.6, zorder=0)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper right", fontsize=10)
fig.tight_layout()
fig.savefig(OUT + "Figure5_moderation_barchart.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ==================================================== FIGURE 6  four variables
fig, ax = plt.subplots(figsize=(6.0, 3.4))
ax.set_xlim(-0.03, 1.03); ax.set_ylim(0, 1.02); ax.axis("off")
Y0, H, W = 0.70, 0.20, 0.26
BOT = Y0 - H / 2
cx = {"X": 0.16, "M": 0.50, "Y": 0.84}
box(ax, cx["X"], Y0, W, H, "Network distance to\nnearest off-premise\noutlet  (X)")
box(ax, cx["M"], Y0, W, H, "Incidental alcohol\npurchases  (M)")
box(ax, cx["Y"], Y0, W, H, "Alcohol spending\nas % of income  (Y)")
for a_, b_, sg in [("X", "M", "–"), ("M", "Y", "+")]:
    x1, x2 = cx[a_] + W / 2, cx[b_] - W / 2
    arrow(ax, (x1, Y0), (x2, Y0))
    ax.text((x1 + x2) / 2, Y0 + (-0.085 if a_ == "X" else 0.065), sg,
            ha="center", fontsize=14, color=INK)
box(ax, 0.33, 0.955, 0.24, 0.10, "Vehicle access  (Z)", fs=9.2, ec=GRAY, lw=1.3)
arrow(ax, (0.33, 0.905), (0.33, 0.765), color=GRAY, lw=1.5, ms=13)
ax.text(0.355, 0.835, "moderates", fontsize=8.6, style="italic", color=GRAY, ha="left")
arrow(ax, (cx["X"], BOT), (cx["Y"], BOT), color=GRAY, lw=1.2,
      ls=(0, (4, 3)), rad=0.42, ms=12)
ax.text(0.50, 0.335, "–   residual direct path (planned, stock-up purchases)",
        ha="center", fontsize=8.6, color=GRAY, style="italic",
        bbox=dict(fc="white", ec="none", pad=2.5))
ax.annotate("", xy=(1.0, 0.13), xytext=(0.0, 0.13),
            arrowprops=dict(arrowstyle="->", color=LIGHT, lw=1.2))
for k_, lab in [("X", "at residential choice"), ("M", "daily / weekly"), ("Y", "past 30 days")]:
    ax.plot([cx[k_]], [0.13], "|", color=LIGHT, ms=8)
    ax.text(cx[k_], 0.06, lab, ha="center", fontsize=8.2, color=GRAY)
ax.text(0.0, 0.185, "time-ordered causal path", fontsize=8.2, color=GRAY, style="italic")
fig.savefig(OUT + "Figure6_four_variable_model.png", dpi=300, bbox_inches="tight")
plt.close(fig)

print("all figures written")
