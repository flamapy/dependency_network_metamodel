
from datetime import datetime

from famapy.core.models import VariabilityElement, VariabilityModel


class Version(VariabilityElement):

    '''
    Version(
        release: str,
        mayor: int,
        minor: int,
        patch: int,
        build_number: int,
        release_date: datetime,
        cves: list[dict],
        count: int,
        packages: list[Package],
    )
    '''

    release: str
    mayor: int
    minor: int
    patch: int
    build_number: int
    release_date: datetime
    cves: list[dict]
    count: int
    packages: list['Package']

    def __init__(self, **kwargs) -> None:
        keys = [
            'release',
            'mayor',
            'minor',
            'patch',
            'build_number',
            'release_date',
            'packages_edges',
            'cves'
        ]
        for key in keys:
            setattr(self, key, kwargs.get(key))

    def __str__(self) -> str:
        return f'{self.release} -- {self.release_date}'


class Package(VariabilityElement):

    '''
    Package(
        name: str,
        versions: list[Version]
    )
    '''

    name: str
    versions: list['Version']

    def __init__(self, **kwargs) -> None:
        valid_keys = [
            'name',
            'versions'
        ]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

    def __str__(self) -> str:
        return f'{self.name}'

class RequirementFile():

    '''
    RequirementFile(
        name: str,
        manager: str,
        packages: list[Package]
    )
    '''

    name: str
    manager: str
    packages: list['Package']

    def __init__(self, **kwargs) -> None:
        valid_keys = [
            'name',
            'manager',
            'packages'
        ]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

    def __str__(self) -> str:
        return f'{self.name} -- {self.manager}'


class DependencyNetwork(VariabilityModel):

    '''
    DependencyNetwork(
        owner: str,
        name: str,
        requirement_files: list[RequirementFile]
    )
    '''

    owner: str
    name: str
    requirement_files: list['RequirementFile']

    @staticmethod
    def get_extension() -> str:
        return 'dn'
    
    def __init__(self, **kwargs) -> None:
        valid_keys = [
            'owner',
            'name',
            'requirement_files'
        ]
        for key in valid_keys:
            setattr(self, key, kwargs.get(key))

    def __str__(self) -> str:
        return f'{self.owner} -- {self.name}'