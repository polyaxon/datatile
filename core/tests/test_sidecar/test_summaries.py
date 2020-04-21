#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

import pytest

from tests.utils import BaseTestCase

from polyaxon.containers.contexts import CONTEXT_MOUNT_ARTIFACTS
from polyaxon.polyboard.artifacts import V1RunArtifact
from polyaxon.polyboard.events import V1Events
from polyaxon.sidecar.outputs.summaries import sync_events_summaries


@pytest.mark.sidecar_mark
class TestEventsSummaries(BaseTestCase):
    def test_metrics_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="metric",
            last_check=None,
        )
        events = V1Events.read(
            name="metric_events",
            kind="metric",
            data=os.path.abspath("tests/fixtures/polyboard/metric/metric_events.plx"),
        )
        assert events.name == "metric_events"
        assert summaries == [
            V1RunArtifact(
                name="metric_events",
                kind="metric",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/metric/metric_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {"metric_events": 0.3}

    def test_images_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="image",
            last_check=None,
        )
        events = V1Events.read(
            name="image_events",
            kind="image",
            data=os.path.abspath("tests/fixtures/polyboard/image/image_events.plx"),
        )
        assert events.name == "image_events"
        assert summaries == [
            V1RunArtifact(
                name="image_events",
                kind="image",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/image/image_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_histograms_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="histogram",
            last_check=None,
        )
        events = V1Events.read(
            name="histogram_events",
            kind="histogram",
            data=os.path.abspath(
                "tests/fixtures/polyboard/histogram/histogram_events.plx"
            ),
        )
        assert events.name == "histogram_events"
        assert summaries == [
            V1RunArtifact(
                name="histogram_events",
                kind="histogram",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/histogram/histogram_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_videos_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="video",
            last_check=None,
        )
        events = V1Events.read(
            name="video_events",
            kind="video",
            data=os.path.abspath("tests/fixtures/polyboard/video/video_events.plx"),
        )
        assert events.name == "video_events"
        assert summaries == [
            V1RunArtifact(
                name="video_events",
                kind="video",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/video/video_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_audios_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="audio",
            last_check=None,
        )
        events = V1Events.read(
            name="audio_events",
            kind="audio",
            data=os.path.abspath("tests/fixtures/polyboard/audio/audio_events.plx"),
        )
        assert events.name == "audio_events"
        assert summaries == [
            V1RunArtifact(
                name="audio_events",
                kind="audio",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/audio/audio_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_htmls_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard", events_kind="html", last_check=None,
        )
        events = V1Events.read(
            name="html_events",
            kind="html",
            data=os.path.abspath("tests/fixtures/polyboard/html/html_events.plx"),
        )
        assert events.name == "html_events"
        assert summaries == [
            V1RunArtifact(
                name="html_events",
                kind="html",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/html/html_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_charts_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="chart",
            last_check=None,
        )
        events = V1Events.read(
            name="chart_events",
            kind="chart",
            data=os.path.abspath("tests/fixtures/polyboard/chart/chart_events.plx"),
        )
        assert events.name == "chart_events"
        assert summaries == [
            V1RunArtifact(
                name="chart_events",
                kind="chart",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/chart/chart_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_curves_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="curve",
            last_check=None,
        )
        events = V1Events.read(
            name="curve_events",
            kind="curve",
            data=os.path.abspath("tests/fixtures/polyboard/curve/curve_events.plx"),
        )
        assert events.name == "curve_events"
        assert summaries == [
            V1RunArtifact(
                name="curve_events",
                kind="curve",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/curve/curve_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_artifacts_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="artifact",
            last_check=None,
        )
        events = V1Events.read(
            name="artifact_events",
            kind="artifact",
            data=os.path.abspath(
                "tests/fixtures/polyboard/artifact/artifact_events.plx"
            ),
        )
        assert events.name == "artifact_events"
        assert summaries == [
            V1RunArtifact(
                name="artifact_events",
                kind="artifact",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/artifact/artifact_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_models_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="model",
            last_check=None,
        )
        events = V1Events.read(
            name="model_events",
            kind="model",
            data=os.path.abspath("tests/fixtures/polyboard/model/model_events.plx"),
        )
        assert events.name == "model_events"
        assert summaries == [
            V1RunArtifact(
                name="model_events",
                kind="model",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/model/model_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}

    def test_dataframes_summaries(self):
        summaries, last_values = sync_events_summaries(
            events_path="tests/fixtures/polyboard",
            events_kind="dataframe",
            last_check=None,
        )
        events = V1Events.read(
            name="dataframe_events",
            kind="dataframe",
            data=os.path.abspath(
                "tests/fixtures/polyboard/dataframe/dataframe_events.plx"
            ),
        )
        assert events.name == "dataframe_events"
        assert summaries == [
            V1RunArtifact(
                name="dataframe_events",
                kind="dataframe",
                connection=None,
                summary=events.get_summary(),
                path=os.path.relpath(
                    "tests/fixtures/polyboard/dataframe/dataframe_events.plx",
                    CONTEXT_MOUNT_ARTIFACTS,
                ),
                is_input=False,
            )
        ]
        assert last_values == {}
