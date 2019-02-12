import activitylogs

from event_manager.events import experiment_group

activitylogs.subscribe(experiment_group.ExperimentGroupCreatedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupUpdatedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupDeletedTriggeredEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupViewedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupArchivedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupRestoredEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupBookmarkedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupUnBookmarkedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupStoppedTriggeredEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupResumedTriggeredEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupExperimentsViewedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupStatusesViewedEvent)
activitylogs.subscribe(experiment_group.ExperimentGroupMetricsViewedEvent)
