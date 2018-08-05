"""
Integrates GRPC client input stream with a Q-Learning framework, then returns the results to the
client.
"""
import client as ct
import brain as bn

# Initializes client and Q-learning model.
client = ct.GrpcClient()
brain = bn.Dqn()

# Starts client listening and gets streamed values.
client.listen()
values = client.values 

# Updates Q-learning model with streamed values, and gets optimized output.
output = brain.update(reward, values)

# Sends optimized output back to client.
client.send_command(output)
