
class UniqueSequencesPlugin:
  def input(self, filename):
       self.fastafile = open(filename, 'r')

  def run(self):
    self.sequences = set()
    lineno = 0
    for line in self.fastafile:
      if (lineno % 2 == 1):
         seq = line.strip()
         self.sequences.add(seq)
      lineno += 1

  def output(self, filename):
      outfile =open(filename, 'w')
      for seq in self.sequences:
         outfile.write(seq+"\n")
