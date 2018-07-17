import auditor

from event_manager.events import tensorboard

auditor.subscribe(tensorboard.TensorboardStartedEvent)
auditor.subscribe(tensorboard.TensorboardStartedTriggeredEvent)
auditor.subscribe(tensorboard.TensorboardSoppedEvent)
auditor.subscribe(tensorboard.TensorboardSoppedTriggeredEvent)
auditor.subscribe(tensorboard.TensorboardViewedEvent)
auditor.subscribe(tensorboard.TensorboardBookmarkedEvent)
auditor.subscribe(tensorboard.TensorboardUnBookmarkedEvent)
auditor.subscribe(tensorboard.TensorboardNewStatusEvent)
auditor.subscribe(tensorboard.TensorboardFailedEvent)
auditor.subscribe(tensorboard.TensorboardSucceededEvent)
