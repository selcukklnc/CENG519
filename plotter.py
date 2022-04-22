import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')
df.drop("SimCnt", axis=1)

by_node_count = df.groupby(by="NodeCount")

avg_value = by_node_count.mean()
std_value = by_node_count.std()

avg_compiletime = avg_value[["CompileTime"]]
std_compiletime = std_value[["CompileTime"]]
node_compile = avg_compiletime.plot(kind="bar", yerr=std_compiletime, colormap='Paired')
node_compile.set_title("Node Count vs Time of Compilation Graph")
node_compile.set_ylabel("Time of Compilation (ms)")
node_compile.set_xlabel("Node Count")
plt.savefig("Node_Count_vs_Compile.png")

avg_keygentime = avg_value[["KeyGenerationTime"]]
std_keygentime = std_value[["KeyGenerationTime"]]
node_keygen = avg_keygentime.plot(kind="bar", yerr=std_keygentime, colormap='Paired')
node_keygen.set_title("Node Count vs Time of Key Generation Graph")
node_keygen.set_ylabel("Time of Key Generation (ms)")
node_keygen.set_xlabel("Node Count")
plt.savefig("Node_Count_vs_KeyGen_Time.png")

avg_encryptiontime = avg_value[["EncryptionTime"]]
std_encryptiontime = std_value[["EncryptionTime"]]
node_encryption = avg_encryptiontime.plot(kind="bar", yerr=std_encryptiontime, colormap='Paired')
node_encryption.set_title("Node Count vs Time of Encryption Graph")
node_encryption.set_ylabel("Time of Encryption (ms)")
node_encryption.set_xlabel("Node Count")
plt.savefig("Node_Count_vs_Encryption.png")

avg_executiontime = avg_value[["ExecutionTime"]]
std_executiontime = std_value[["ExecutionTime"]]
node_execution = avg_executiontime.plot(kind="bar", yerr=std_executiontime, colormap='Paired')
node_execution.set_title("Node Count vs Time of Execution Graph")
node_execution.set_ylabel("Time of Execution (ms)")
node_execution.set_xlabel("Node Count")
plt.savefig("Node_Count_vs_Execution.png")

avg_decryptiontime = avg_value[["DecryptionTime"]]
std_decryptiontime = std_value[["DecryptionTime"]]
node_decryption = avg_decryptiontime.plot(kind="bar", yerr=std_decryptiontime, colormap='Paired')
node_decryption.set_title("Node Count vs Time of Decryption Graph")
node_decryption.set_ylabel("Time of Decryption (ms)")
node_decryption.set_xlabel("Node Count")
plt.savefig("Node_Count_vs_Decryption.png")

avg_refexe_time = avg_value[["ReferenceExecutionTime"]]
std_refexe_time = std_value[["ReferenceExecutionTime"]]
node_reference_execution = avg_refexe_time.plot(kind="bar", yerr=std_refexe_time, colormap='Paired')
node_reference_execution.set_title("Node Count vs Time of Reference Execution Graph")
node_reference_execution.set_xlabel("Node Count")
node_reference_execution.set_ylabel("Time of Reference Execution (ms)")
plt.savefig("Node_Count_vs_Reference_Execution.png")

avg_mse = avg_value[["Mse"]]
std_mse = std_value[["Mse"]]
node_mse = avg_mse.plot(kind="bar", yerr=std_mse, colormap='Paired')
node_mse.set_title("Node Count vs MSE Graph")
node_mse.set_xlabel("Node Count")
node_mse.set_ylabel("MSE")
plt.savefig("Node_Count_vs_MSE.png")