DEFAULT_WINDOW_SIZE = 32
DEFAULT_THRESHOLD_MIN = 45.39
DEFAULT_THRESHOLD_MAX = 46.0
DEFAULT_MAX_EVALUE = 0.00445
DEFAULT_PENALTY_BLACK = 2.2
DEFAULT_PENALTY_WHITE = 0.7
DEFAULT_BLACK_LIST = ['VOG0496', 'VOG5264', 'VOG4730', 'VOG5818', 'VOG7281', \
                      'VOG6063', 'VOG6030', 'VOG1710', 'VOG0996', 'VOG4524', \
                      'VOG8021', 'VOG8536', 'VOG2368', 'VOG1850', 'VOG1031', \
                      'VOG0985', 'VOG0274', 'VOG4344', 'VOG1844', 'VOG0088', \
                      'VOG8607', 'VOG4615', 'VOG8992', 'VOG3235', 'VOG0092', \
                      'VOG4155', 'VOG3532', 'VOG1045', 'VOG4149', 'VOG8062', \
                      'VOG4562', 'VOG7442', 'VOG7446', 'VOG0419', 'VOG4319', \
                      'VOG8429', 'VOG4409', 'VOG1422', 'VOG10018', 'VOG3101',\
                      'VOG5441', 'VOG4469', 'VOG6988', 'VOG4678', 'VOG3722']
DEFAULT_WHITE_LIST = ["VOG0568", "VOG0569", "VOG0565", "VOG0566", "VOG0567", "VOG0562", "VOG2703", "VOG0968", \
                        "VOG0700", "VOG0701", "VOG0703", "VOG0704", "VOG8223", "VOG9502", "VOG5046", "VOG5260", \
                        "VOG4643", "VOG4645", "VOG4647", "VOG9348", "VOG3606", "VOG9762", "VOG4736", "VOG3424", \
                        "VOG9962", "VOG8568", "VOG7616", "VOG7615", "VOG6418", "VOG7437", "VOG10916", "VOG6520", \
                        "VOG9667", "VOG0825", "VOG0824", "VOG0827", "VOG0559", "VOG0557", "VOG2779", "VOG4545", \
                        "VOG0953", "VOG1159", "VOG0602", "VOG5254", "VOG0044", "VOG4652", "VOG4659", "VOG3309", \
                        "VOG4438", "VOG2545", "VOG10850", "VOG1942", "VOG1319", "VOG3891", "VOG3890", "VOG2388", \
                        "VOG3892", "VOG3894", "VOG3897", "VOG2166", "VOG1837", "VOG0541", "VOG0947", "VOG0945", \
                        "VOG0723", "VOG0720", "VOG0727", "VOG0724", "VOG0725", "VOG0837", "VOG0835", "VOG0832", \
                        "VOG0833", "VOG0830", "VOG0831", "VOG0838", "VOG0839", "VOG0618", "VOG0614", "VOG0615", \
                        "VOG5060", "VOG0583", "VOG0051", "VOG0054", "VOG5660", "VOG4829", "VOG4828", "VOG4820", \
                        "VOG8497", "VOG0588", "VOG3622", "VOG3396", "VOG4757", "VOG3401", "VOG3406", "VOG3409", \
                        "VOG2119", "VOG1956", "VOG0536", "VOG0534", "VOG0539", "VOG0283", "VOG0843", "VOG0842", \
                        "VOG0847", "VOG0848", "VOG0198", "VOG0195", "VOG10933", "VOG9374", "VOG4630", "VOG4632", \
                        "VOG4633", "VOG4634", "VOG10054", "VOG10059", "VOG5621", "VOG8445", "VOG6866", "VOG0524", \
                        "VOG0526", "VOG6440", "VOG0840", "VOG0298", "VOG0299", "VOG0292", "VOG0296", "VOG0850", \
                        "VOG0855", "VOG0186", "VOG0181", "VOG0189", "VOG9547", "VOG0275", "VOG5357", "VOG10608", \
                        "VOG5734", "VOG4609", "VOG4606", "VOG4600", "VOG4602", "VOG3379", "VOG4171", "VOG4994", \
                        "VOG4999", "VOG8520", "VOG4771", "VOG4772", "VOG8855", "VOG6876", "VOG0519", "VOG0518", \
                        "VOG0514", "VOG2644", "VOG0641", "VOG5994", "VOG4618", "VOG4619", "VOG4612", "VOG3699", \
                        "VOG9474", "VOG4986", "VOG7882", "VOG4763", "VOG2341", "VOG10969", "VOG2124", "VOG2125", \
                        "VOG6600", "VOG1900", "VOG2015", "VOG0650", "VOG0651", "VOG0655", "VOG5023", "VOG5027", \
                        "VOG10898", "VOG0254", "VOG1309", "VOG9583", "VOG8509", "VOG4573", "VOG4572", "VOG0952", \
                        "VOG4888", "VOG4799", "VOG2337", "VOG2336", "VOG2339", "VOG2338", "VOG7693", "VOG1912", \
                        "VOG1915", "VOG1047", "VOG1049", "VOG2790", "VOG2793", "VOG2086", "VOG2795", "VOG2794", \
                        "VOG0790", "VOG0796", "VOG0799", "VOG0221", "VOG0227", "VOG0226", "VOG4364", "VOG4361", \
                        "VOG9227", "VOG5942", "VOG4563", "VOG4564", "VOG4565", "VOG4566", "VOG4567", "VOG4568", \
                        "VOG4890", "VOG3327", "VOG3328", "VOG6138", "VOG7440", "VOG7686", "VOG6001", "VOG2788", \
                        "VOG0800", "VOG1320", "VOG1329", "VOG9609", "VOG9857", "VOG4555", "VOG4557", "VOG4556", \
                        "VOG4550", "VOG4553", "VOG4552", "VOG3798", "VOG8306", "VOG7238", "VOG6545", "VOG6495", \
                        "VOG0939", "VOG4559", "VOG1887", "VOG5029", "VOG5092", "VOG5096", "VOG5095", "VOG0753", \
                        "VOG1333", "VOG4544", "VOG2791", "VOG3498", "VOG10343", "VOG3304", "VOG3652", "VOG3651", \
                        "VOG3477", "VOG3478", "VOG8337", "VOG8336", "VOG10230", "VOG0251", "VOG6153", "VOG6154", \
                        "VOG1433", "VOG0327", "VOG0322", "VOG0321", "VOG6203", "VOG0528", "VOG5084", "VOG4672", \
                        "VOG1348", "VOG9470", "VOG0696", "VOG0697", "VOG0695", "VOG0692", "VOG0691", "VOG0698", \
                        "VOG0107", "VOG4684", "VOG9305", "VOG4593", "VOG4596", "VOG4599", "VOG4598", "VOG4845", \
                        "VOG4841", "VOG3480", "VOG3648", "VOG3649", "VOG3644", "VOG3313", "VOG3461", "VOG3462", \
                        "VOG3468", "VOG8923", "VOG10227", "VOG7569", "VOG0356", "VOG0355", "VOG1350", "VOG1352", \
                        "VOG1353", "VOG1356", "VOG5155", "VOG4693", "VOG4690", "VOG4691", "VOG4694", "VOG4699", \
                        "VOG2165", "VOG2163", "VOG9315", "VOG9317", "VOG4589", "VOG4586", "VOG4581", "VOG8134", \
                        "VOG8354", "VOG2215", "VOG3298", "VOG11077", "VOG1637", "VOG1638", "VOG7483", "VOG2186", \
                        "VOG2188", "VOG1183", "VOG0582", "VOG1298", "VOG0584", "VOG0585", "VOG1563", "VOG0901", \
                        "VOG0764", "VOG0765", "VOG5443", "VOG0010", "VOG4002", "VOG4005", "VOG4862", "VOG4865", \
                        "VOG5996", "VOG4716", "VOG4713", "VOG4711", "VOG8340", "VOG8904", "VOG3287", "VOG4605", \
                        "VOG6163", "VOG2154", "VOG2153", "VOG6181", "VOG0801", "VOG0577", "VOG0574", "VOG0573", \
                        "VOG0572", "VOG0571", "VOG0977", "VOG0976", "VOG0152", "VOG0397", "VOG0204", "VOG0021", \
                        "VOG0025", "VOG0026", "VOG3616", "VOG4705", "VOG4701", "VOG3434", "VOG2792", "VOG3721", \
                        "VOG3549", "VOG2142", "VOG10904", "VOG2149", "VOG2096", "VOG9438"]
