python /work/jmalekar/scale-sim-v2/scalesim/scale_decoder.py -ts /work/jmalekar/scale-sim-v2/topologies/opt_models -c /work/jmalekar/scale-sim-v2/configs/cloud/is.cfg > opt_cloud_is.txt
python /work/jmalekar/scale-sim-v2/scalesim/scale_decoder.py -ts /work/jmalekar/scale-sim-v2/topologies/opt_models -c /work/jmalekar/scale-sim-v2/configs/cloud/ws.cfg > opt_cloud_ws.txt
python /work/jmalekar/scale-sim-v2/scalesim/scale_decoder.py -ts /work/jmalekar/scale-sim-v2/topologies/opt_models -c /work/jmalekar/scale-sim-v2/configs/cloud/os.cfg > opt_cloud_os.txt

python /work/jmalekar/scale-sim-v2/scalesim/scale_decoder.py -ts /work/jmalekar/scale-sim-v2/topologies/opt_models -c /work/jmalekar/scale-sim-v2/configs/edge/is.cfg > opt_edge_is.txt
python /work/jmalekar/scale-sim-v2/scalesim/scale_decoder.py -ts /work/jmalekar/scale-sim-v2/topologies/opt_models -c /work/jmalekar/scale-sim-v2/configs/edge/ws.cfg > opt_edge_ws.txt
python /work/jmalekar/scale-sim-v2/scalesim/scale_decoder.py -ts /work/jmalekar/scale-sim-v2/topologies/opt_models -c /work/jmalekar/scale-sim-v2/configs/edge/os.cfg > opt_edge_os.txt