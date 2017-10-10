from config.server import IDLE_CONNECTION_TIMEOUT
from core import FM


class DownloadFiles(FM.BaseAction):
    def __init__(self, request, paths, session, mode, **kwargs):
        super(DownloadFiles, self).__init__(request=request, **kwargs)

        self.paths = paths
        self.session = session
        self.mode = mode

    def run(self):
        request = self.get_rpc_request()
        request.set_timeout(IDLE_CONNECTION_TIMEOUT)
        result = request.request('webdav/download_files', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), paths=self.paths, mode=self.mode,
                                 session=self.session)
        answer = self.process_result(result)
        return answer
