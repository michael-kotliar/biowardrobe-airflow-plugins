#!/usr/bin/env python3
from cwl_airflow_parser.cwldag import CWLDAG
from biowardrobe_airflow_plugins.operators.biowardrobepluginjobdispatcher import BioWardrobePluginJobDispatcher
from biowardrobe_airflow_plugins.operators.biowardrobepluginjobgatherer import BioWardrobePluginJobGatherer
from biowardrobe_airflow_plugins.utils.func import get_workflow_by_name


def create_plugin(workflow_name):
    dag = CWLDAG(default_args={'pool': 'biowardrobe_plugins'},
                 cwl_workflow = get_workflow_by_name(workflow_name))
    dag.create()
    dag.add(BioWardrobePluginJobDispatcher(dag=dag), to='top')
    dag.add(BioWardrobePluginJobGatherer(dag=dag), to='bottom')
    return dag
