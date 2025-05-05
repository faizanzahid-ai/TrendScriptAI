

import grpc
from concurrent import futures
import asyncio
import os

import pipeline_pb2_pb2
import pipeline_pb2_pb2_grpc

from app_pipeline import run_pipeline  # Your original `main()` logic extracted as a callable

class StoryPipelineServicer(pipeline_pb2_pb2_grpc.StoryPipelineServicer):

    async def async_run_pipeline(self, request):
        try:
            output_file = await run_pipeline(
                keywords=request.keywords,
                themes=request.themes,
                regions=request.regions,
                max_results=request.max_results,
                num_random=request.num_random_videos,
                custom_prompt=request.custom_prompt if request.custom_prompt else None
            )
            return pipeline_pb2_pb2.GenerateReply(
                status="success",
                message="Pipeline completed successfully.",
                output_file=output_file
            )
        except Exception as e:
            return pipeline_pb2_pb2.GenerateReply(
                status="error",
                message=str(e),
                output_file=""
            )

    def Generate(self, request, context):
        return asyncio.run(self.async_run_pipeline(request))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pipeline_pb2_pb2_grpc.add_StoryPipelineServicer_to_server(StoryPipelineServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("🚀 gRPC server is running on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

