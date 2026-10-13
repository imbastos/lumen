from attrs import define

from enums.riasec_profile import RiasecProfile


@define
class RiasecQuestion:
    profile: RiasecProfile
    text: str
