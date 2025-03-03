from analysis_tools import ObjectCollection, Category, Process, Dataset, Feature, Systematic
from plotting_tools import Label

from cmt.config.base_config import Config as cmt_config

class Config(cmt_config):
    def add_categories(self):
        categories = [
            Category("base", "base", selection="event >= 0"),
        ]
        return ObjectCollection(categories)

    def add_processes(self):
        processes = [
            Process("ditauonium", Label("Ditauonium"), color=(96, 96, 96), isSignal=True),
        ]
        
        process_group_names = {
            "default": [
                "ditauonium"
            ],
        }
        return ObjectCollection(processes), process_group_names, {}

    def add_datasets(self):
        datasets = [
            Dataset("ditauonium",
                dataset="/ditauonium_14TeV/sawan-Nanotron-Fix-cdd9ad1a7648d3a5f06c1b94d96e2f7e/USER",
                process=self.processes.get("ditauonium"),
                xs=3.67,  # Check with David
                check_empty=False,
            ),
        ]
        return ObjectCollection(datasets)

    def add_features(self):
        features = [
            Feature("gen_leadmuon_pt",
                "Max(GenPart_pt[abs(GenPart_pdgId) == 13])",
                binning=(56, 0, 40),
                x_title=Label("Generated leadmuon #pt"),
            ),
            Feature("gen_leadmuon_eta", 
                "GenPart_eta[ArgMax(GenPart_pt[abs(GenPart_pdgId) == 13])]",
                binning=(56, -7, 7),
                x_title=Label("Generated Lead Muon eta"),
            Feature("gen_ditauonium_eta",
                "GenPart_eta[GenPart_pdgId == 15153 && GenPart_status == 62]",
                binning=(56, -7, 7),
                x_title=Label("Generated ditauonium #eta"),
            ),
        ]
        return ObjectCollection(features)

    def add_weights(self):
        weights = DotDict()
        weights.default = "1"

        weights.total_events_weights = ["1"]
        weights.base = ["1"]
        return weights

config = Config("base", year=2022, ecm=14, lumi_pb=300000)
