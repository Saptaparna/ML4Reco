# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:phase2_realistic_T15 -n 10 --era Phase2C9 --eventcontent FEVTDEBUG --runUnscheduled -s RAW2DIGI,L1Reco,RECO,RECOSIM --datatier GEN-SIM-RECO --pileup AVE_200_BX_25ns --geometry Extended2026D49 --no_exec --python_filename=RECO_fragment.py
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('RECO',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cmseos.fnal.gov///store/user/lpchgcal/sapta/TimingSamples/MachineLearning/TauTime_step1/step1_Tau_EEnergy_nNEVENT_partNPART.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step2_Tau_EEnergy_nNEVENT_partNPART.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)
process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")
# append the HGCTruthProducer to the recosim step

process.FEVTDEBUGoutput.outputCommands.append("keep *_*G4*_*_*")
process.FEVTDEBUGoutput.outputCommands.append("keep SimClustersedmAssociation_mix_*_*")
process.FEVTDEBUGoutput.outputCommands.append("keep CaloParticlesedmAssociation_mix_*_*")

# Additional output definition
process.FEVTDEBUGoutput.outputCommands.append("keep *_*G4*_*_*")
process.FEVTDEBUGoutput.outputCommands.extend(["keep *_MergedTrackTruth_*_*",
    "keep *_trackingParticleRecoTrackAsssociation_*_*",
    "keep *_hgcRecHitsToSimClusters_*_*",
    "keep SimClustersedmAssociation_mix_*_*", "keep CaloParticlesedmAssociation_mix_*_*",
    "keep *_pfParticles_*_*",
    "keep recoPFRecHits_*_*_*",
    "keep *_hgcSimTruth_*_*",
    "keep *_lcAssocByEnergyScoreProcer_*_*",
    "keep *_layerClusterCaloParticleAssociationProducer_*_*",
    "keep *_scAssocByEnergyScoreProducer_*_*",
    "keep *_layerClusterSimClusterAssociationProducer_*_*",
])

# Other statements
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-3)
process.mix.maxBunch = cms.int32(3)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.recosim_step,process.endjob_step,process.FEVTDEBUGoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
