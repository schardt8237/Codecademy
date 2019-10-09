import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

rottweiler_tl = fetchmaker.get_weight("rottweiler")

print 
print np.mean(rottweiler_tl)
print np.std(rottweiler_tl)

whippet_rescue = fetchmaker.get_is_rescue("whippet")

num_whippet_rescues = np.count_nonzero(whippet_rescue==1)
num_whippets = np.size(whippet_rescue)

pval = binom_test(num_whippets, n=10000, p=0.08)
print pval

whippets = fetchmaker.get_weight("whippet")
terriers = fetchmaker.get_weight("terrier")
pitbulls = fetchmaker.get_weight("pitbull")

fstat, pval = f_oneway(whippets, terriers, pitbulls)
print pval

v = np.concatenate([whippets, terriers, pitbulls])
labels = ['Whippets'] * len(whippets) + ['Terriers'] * len(terriers) + ['Pitbulls'] * len(pitbulls)

tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print tukey_results

poodle_colors = fetchmaker.get_color("poodle")
shihtzu_colors = fetchmaker.get_color("shihtzu")

num_black_poodle = np.count_nonzero(poodle_colors == "black")
num_brown_poodle = np.count_nonzero(poodle_colors == "brown")
num_gold_poodle = np.count_nonzero(poodle_colors == "gold")
num_grey_poodle = np.count_nonzero(poodle_colors == "grey")
num_white_poodle = np.count_nonzero(poodle_colors == "white")

num_black_shihtzu = np.count_nonzero(shihtzu_colors == "black")
num_brown_shihtzu = np.count_nonzero(shihtzu_colors == "brown")
num_gold_shihtzu = np.count_nonzero(shihtzu_colors == "gold")
num_grey_shihtzu = np.count_nonzero(shihtzu_colors == "grey")
num_white_shihtzu = np.count_nonzero(shihtzu_colors == "white")

color_table = [[num_black_poodle, num_black_shihtzu],
               [num_brown_poodle, num_brown_shihtzu],
               [num_gold_poodle, num_gold_shihtzu],
               [num_grey_poodle, num_grey_shihtzu],
               [num_white_poodle, num_white_shihtzu]]

print color_table

_, pvalue, _, _ = chi2_contingency(color_table)
print pvalue