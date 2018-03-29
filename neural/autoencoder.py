from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers import BackpropTrainer


def main():
    ds = SupervisedDataSet(1, 1)  # (num_input_neurons, num_output_neurons)

    for i in range(1, 9):
        ds.addSample((i,), (i,))

    net = buildNetwork(1, 8, 1, hiddenclass=TanhLayer)

    trainer = BackpropTrainer(net, ds)

    trainer.trainUntilConvergence(verbose=False,
                                  validationProportion=0.15,
                                  maxEpochs=1000,
                                  continueEpochs=10)

    print(net.activateOnDataset(ds))
    # print(net.activate((-100, )))


if __name__ == '__main__':
    main()
