# Brandeis CS/CL Ph.D. Seminars Website

This repository contains the data and scripts needed to build the [website for the Brandeis CS/CL Ph.D. seminars](http://rm.cab/seminars). The site is built from a data file, `data.json`, and a folder of PDFs, `papers`.

The `data.json` file contains simple entries for each seminar:
```json
{ "title": "Neural Discourse Parsing",
  "speaker": "Te Rutherford",
  "url": "http://www.cs.brandeis.edu/~tet/",
  "date": "March 23rd, 2016",
  "abstract": "Inferring  implicit  discourse  relations  in natural language text is the most difficult subtask in discourse parsing.   Many neural network models have been proposed to tackle  this  problem.   However,  the  comparison  for  this  task  is  not  unified,  so we  could  hardly  draw  clear  conclusions about  the  effectiveness  of  various  architectures.    Here,  we  propose  neural  network  models  that  are  based  on  feedforward and long-short term memory architecture and systematically study the effects of varying structures.  To our surprise, the best-configured  feedforward  architecture outperforms  LSTM-based  model  in  most cases  despite  thorough  tuning.    Further, we compare our best feedforward system with competitive convolutional and recurrent  networks  and  find  that  feedforward can actually be more effective. For the first time  for  this  task,  we  compile  and  publish outputs from previous neural and non-neural systems to establish the standard for further comparison.",
  "paper": "neural_discourse_final.pdf"
}
```

The `paper` field refers to the name of a PDF in the `papers` folder. To build the website:

```bash
# install needed dependencies
pipenv shell
pipenv install

# run the script
make
```

The website will be rendered and placed in the `output` directory. The `make deploy` option automatically SCPs the files to the Brandeis webserver.
