#! /bin/bash

oc new-project kafka ;
kubectl create -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka ;
kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-persistent-single.yaml -n kafka ;

