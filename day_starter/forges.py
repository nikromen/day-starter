from abc import ABC, abstractmethod


class GitForge(ABC):
    @abstractmethod
    def show_requests(self) -> list[str]:
        ...


class GitHub(GitForge):
    pass


class GitLab(GitForge):
    pass


class _PagureAPI:
    pass


class Pagure(GitForge):
    pass
