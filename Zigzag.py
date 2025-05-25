print("name:aditya.M,USN:1AY24AI004,sec:'M")
def run_zigzag(num_asterisks):
  indentation=0
  direction=1 # 1 for increasing,-1 for decreasimg
  while num_asterisks > 0:
   print(" "*indentation + "*")
   indentation+=direction
   num_asterisks-=1
  if indentation==0 or indentation==5:#adjust upper limit as needed
     direction*=-1
run_zigzag(50)