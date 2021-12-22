"""Binary sensor that represents connection to camera."""
from __future__ import annotations

from typing import TYPE_CHECKING

from viseron.domains.camera import EVENT_STATUS
from viseron.helpers.entity.binary_sensor import BinarySensorEntity

if TYPE_CHECKING:
    from viseron import EventData, Viseron

    from . import AbstractCamera


class CameraBinarySensor(BinarySensorEntity):
    """Base class that is tied to a specific AbstractCamera."""

    def __init__(self, vis: Viseron, camera: AbstractCamera):
        self._vis = vis
        self._camera = camera

        self.device_name = camera.name
        self.device_identifiers = [camera.identifier]


class ConnectionStatusBinarySensor(CameraBinarySensor):
    """Entity that keeps track of connection to camera."""

    def __init__(self, vis: Viseron, camera: AbstractCamera):
        super().__init__(vis, camera)
        self.device_class = "connectivity"
        self.object_id = f"{camera.identifier}_connected"
        self.name = f"{camera.name} Connected"

        vis.listen_event(
            EVENT_STATUS.format(camera_identifier=camera.identifier),
            self.handle_event,
        )

    @property
    def _is_on(self):
        return self._camera.connected

    def handle_event(self, _: EventData):
        """Handle status event."""
        self.set_state()
